from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import connection
from django.contrib import messages
from django.db import IntegrityError


# 检查用户是否是管理员
def is_admin(user):
    return user.is_superuser


# 获取用户列表（登录用户都可访问）
@login_required
def user_list(request):
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT e.id, e.name, 
                   s.name AS supervisor_name, 
                   d.name AS department_name
            FROM employee_employee e, 
                 employee_employee s, 
                 employee_department d
            WHERE e.supervisor_id = s.id
              AND e.department_id = d.id;

            """
        )
        queryset = cursor.fetchall()
    return render(request, 'user_list.html', {"queryset": queryset})


@login_required
@user_passes_test(is_admin)
def user_add(request):
    if request.method == "GET":
        # 获取所有上级和部门
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name FROM employee_employee")
            supervisors = cursor.fetchall()

            cursor.execute("SELECT id, name FROM employee_department")
            departments = cursor.fetchall()

        return render(request, 'user_add.html', {'supervisors': supervisors, 'departments': departments})

    # 获取表单数据
    name = request.POST.get("name")
    supervisor = request.POST.get("supervisor")
    department = request.POST.get("department")

    try:
        # 插入数据到数据库
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO employee_employee (name, supervisor_id, department_id) VALUES (%s, %s, %s)",
                [name, supervisor, department]
            )
        messages.success(request, '用户添加成功！')  # 成功信息
    except IntegrityError as e:
        # 捕获数据库的完整性错误，比如重复数据或外键约束
        messages.error(request, '添加用户失败，数据库错误！请检查输入的数据。')  # 错误信息
    except Exception as e:
        messages.error(request, f'发生错误: {str(e)}')  # 其他错误

    return redirect('/user/list/')


# 编辑用户（仅管理员）
@login_required
@user_passes_test(is_admin)
def user_edit(request, nid):
    if request.method == "GET":
        with connection.cursor() as cursor:
            # 获取当前用户的信息，包括上级和部门信息
            cursor.execute(
                """
                SELECT e.id, e.name, e.supervisor_id, e.department_id,
                       s.name AS supervisor_name, d.name AS department_name
                FROM employee_employee e
                LEFT JOIN employee_employee s ON e.supervisor_id = s.id
                LEFT JOIN employee_department d ON e.department_id = d.id
                WHERE e.id = %s
                """,
                [nid]
            )
            row_object = cursor.fetchone()

            # 获取所有可选的上级员工列表
            cursor.execute("SELECT id, name FROM employee_employee")
            supervisors = cursor.fetchall()

            # 获取所有可选的部门列表
            cursor.execute("SELECT id, name FROM employee_department")
            departments = cursor.fetchall()

        return render(request, 'user_edit.html', {
            "row_object": row_object,
            "supervisors": supervisors,
            "departments": departments
        })

    # 获取表单数据
    name = request.POST.get("name")
    supervisor = request.POST.get("supervisor") or None  # 空值处理
    department = request.POST.get("department") or None  # 空值处理

    # 更新数据库记录
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE employee_employee SET name = %s, supervisor_id = %s, department_id = %s WHERE id = %s",
            [name, supervisor, department, nid]
        )

    return redirect('/user/list/')


# 删除用户（仅管理员）
@login_required
@user_passes_test(is_admin)
def user_delete(request, nid):
    # 检查是否存在关联的考勤或薪资记录
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM employee_attendance WHERE employee_id = %s", [nid])
        attendance_count = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM employee_salary WHERE employee_id = %s", [nid])
        salary_count = cursor.fetchone()[0]

    if attendance_count > 0 or salary_count > 0:
        messages.error(request, "无法删除该用户，存在相关的考勤或薪资记录！")
        return redirect('/user/list/')

    # 删除用户记录
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM employee_employee WHERE id = %s", [nid])
    messages.success(request, "用户已成功删除！")
    return redirect('/user/list/')


# 查看用户考勤记录和薪资
@login_required
def user_attendance_salary(request, nid):
    with connection.cursor() as cursor:
        # 获取员工考勤记录并连接员工姓名
        cursor.execute("""
            SELECT a.id, a.year, a.month, a.employee_id, a.late_days, a.early_leave_days, a.leave_days, a.overtime_hours,
                   e.name AS employee_name
            FROM employee_attendance a
            LEFT JOIN employee_employee e ON a.employee_id = e.id
            WHERE a.employee_id = %s
        """, [nid])
        attendance_queryset = cursor.fetchall()

        # 获取员工工资记录并连接部门名称
        cursor.execute("""
            SELECT s.id, s.year, s.month, s.employee_id, s.department_id, s.base_salary, s.housing_allowance,
                   s.gross_salary, s.deductions, s.net_salary, d.name AS department_name , e.name AS employee_name
            FROM employee_salary s
            LEFT JOIN employee_department d ON s.department_id = d.id
            LEFT JOIN employee_employee e ON s.employee_id = e.id
            WHERE s.employee_id = %s
        """, [nid])
        salary_queryset = cursor.fetchall()

        # 获取系统配置
        cursor.execute("SELECT * FROM employee_systemconfig LIMIT 1")
        system_config = cursor.fetchone()

    return render(request, 'user_attendance_salary.html', {
        "queryset1": attendance_queryset,
        "queryset2": salary_queryset,
        "system_config": system_config
    })


# 用户搜索
@login_required
def user_search(request):
    search_query = request.GET.get('search', '')
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT e.id, e.name, s.name AS supervisor_name, d.name AS department_name
            FROM employee_employee e
            LEFT JOIN employee_employee s ON e.supervisor_id = s.id
            LEFT JOIN employee_department d ON e.department_id = d.id
            WHERE e.name LIKE %s
            """,
            [f"%{search_query}%"]
        )
        queryset = cursor.fetchall()
    return render(request, 'user_list.html', {'queryset': queryset, 'search_query': search_query})
