from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import connection
from django.contrib import messages
from django.db import IntegrityError
# 检查用户是否为管理员
def is_admin(user):
    return user.is_superuser  # 如果用户是管理员，返回True

@login_required
def depart_list(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, name FROM employee_department")
        queryset = cursor.fetchall()
    return render(request, 'depart_list.html', {'queryset': queryset})

@login_required  # 确保用户已登录
@user_passes_test(is_admin)  # 确保只有管理员可以访问
def depart_add(request):
    if request.method == "GET":
        return render(request, 'depart_add.html')

    # 获取用户POST提交过来的数据
    title = request.POST.get("title")
    dept_id = request.POST.get("id")

    # 处理错误
    if not title or not dept_id:
        error_message = "部门名称和ID不能为空！"
        return render(request, 'depart_add.html', {"error_message": error_message})

    try:
        # 保存到数据库
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO employee_department (id, name) VALUES (%s, %s)", [dept_id, title])
    except IntegrityError as e:
        # 捕获数据库约束错误，比如重复的ID
        error_message = "保存失败：该部门ID已经存在！"
        return render(request, 'depart_add.html', {"error_message": error_message})
    except Exception as e:
        # 捕获其他任何未知的错误
        error_message = f"发生错误：{str(e)}"
        return render(request, 'depart_add.html', {"error_message": error_message})

    # 成功后重定向回部门列表
    return redirect("/depart/list/")
@login_required  # 确保用户已登录
@user_passes_test(is_admin)  # 确保只有管理员可以访问
def depart_delete(request):
    nid = request.GET.get("nid")

    # 检查是否有员工与该部门关联
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM employee_employee WHERE department_id = %s", [nid])
        employee_count = cursor.fetchone()[0]

    # 如果部门中有员工，给出提示信息
    if employee_count > 0:
        messages.error(request, "无法删除该部门，存在与该部门关联的员工！")
        return redirect("/depart/list/")  # 重定向回部门列表页面

    # 如果没有关联员工，删除部门
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM employee_department WHERE id = %s", [nid])
    messages.success(request, "部门已成功删除！")
    return redirect("/depart/list/")  # 删除后重定向回部门列表页面

@login_required  # 确保用户已登录
@user_passes_test(is_admin)  # 确保只有管理员可以访问
def depart_edit(request, nid):
    if request.method == "GET":
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name FROM employee_department WHERE id = %s", [nid])
            row_object = cursor.fetchone()
        return render(request, 'depart_edit.html', {"row_object": row_object})

    name = request.POST.get("name")

    with connection.cursor() as cursor:
        cursor.execute("UPDATE employee_department SET name = %s WHERE id = %s", [name, nid])
    return redirect("/depart/list/")

@login_required  # 确保用户已登录
def depart_search(request):
    search_query = request.GET.get('search', '')  # 获取查询参数
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, name FROM employee_department WHERE name LIKE %s", [f"%{search_query}%"])
        queryset = cursor.fetchall()
    return render(request, 'depart_list.html', {'queryset': queryset, 'search_query': search_query})