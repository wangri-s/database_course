from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import connection
from django import forms
from employee import models
from django.http import JsonResponse

# 检查用户是否为管理员
def is_admin(user):
    return user.is_superuser  # 如果用户是管理员，返回True


def get_system_config():
    """使用 SQL 获取系统配置"""
    with connection.cursor() as cursor:
        cursor.execute("""SELECT * FROM employee_systemconfig LIMIT 1""")
        result = cursor.fetchone()

    if not result:
        raise ValueError("系统配置未找到")

    # 将结果转换为字典或类似结构（可以直接按字段名访问）
    system_config = {
        'id': result[0],
        'work_days_per_month': result[1],
        'late_deduction_rate': result[2],
        'early_leave_deduction_rate': result[3],
        'leave_deduction_rate': result[4],
        'overtime_bonus_rate': result[5],
    }

    return system_config


def get_attendance(employee_id, year, month):
    """获取员工的考勤记录"""
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM employee_attendance
            WHERE employee_id = %s AND year = %s AND month = %s
        """, [employee_id, year, month])
        result = cursor.fetchone()
    if not result:
        raise ValueError("该员工在指定月份没有考勤记录")
    return result


def calculate_salary(employee_id, year, month, base_salary, housing_allowance):
    """
    根据员工信息、年份、月份和工资配置计算工资。
    加入加班费用的计算。
    """
    # 获取系统配置，这里使用的是 SQL 获取的字典
    system_config = get_system_config()

    # 获取考勤记录
    attendance = get_attendance(employee_id, year, month)

    # 从考勤记录中提取数据
    late_days = attendance[5] if attendance[5] is not None else 0
    early_leave_days = attendance[6] if attendance[6] is not None else 0
    leave_days = attendance[7] if attendance[7] is not None else 0
    overtime_hours = attendance[8] if attendance[8] is not None else 0

    # 计算扣款
    deductions = (late_days * system_config['late_deduction_rate']) + \
                 (early_leave_days * system_config['early_leave_deduction_rate'])

    # 超过最大请假天数的额外扣款
    max_leave_days = 3
    if leave_days > max_leave_days:
        extra_leave_days = leave_days - max_leave_days
        deductions += extra_leave_days * system_config['leave_deduction_rate']

    # 计算加班费用
    overtime_bonus = overtime_hours * system_config['overtime_bonus_rate']

    # 应发工资和实发工资
    gross_salary = base_salary + housing_allowance + overtime_bonus
    net_salary = gross_salary - deductions

    return gross_salary, deductions, net_salary


class SalaryModelForm(forms.ModelForm):
    class Meta:
        model = models.EmployeeSalary
        fields = ["id", "year", "month", "employee", "department", "base_salary", "housing_allowance", "gross_salary",
                  "deductions", "net_salary"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name != 'id':
                field.widget.attrs = {"class": "form-control"}

        # 设置基础薪资和住房补贴为必填项目
        self.fields['base_salary'].required = True
        self.fields['housing_allowance'].required = True

        # 设置 employee 和 department 的下拉框选项
        self.fields['employee'].queryset = models.EmployeeEmployee.objects.all()
        self.fields['employee'].label = "员工姓名"  # 自定义字段标签
        self.fields['employee'].widget.attrs.update({"class": "form-select"})  # 引入下拉框样式

        self.fields['department'].queryset = models.EmployeeDepartment.objects.all()
        self.fields['department'].label = "部门名称"  # 自定义字段标签
        self.fields['department'].widget.attrs.update({"class": "form-select"})  # 引入下拉框样式


    def clean(self):
        cleaned_data = super().clean()
        base_salary = cleaned_data.get('base_salary')
        housing_allowance = cleaned_data.get('housing_allowance')
        employee = cleaned_data.get('employee')
        year = cleaned_data.get('year')
        month = cleaned_data.get('month')

        attendance = get_attendance(employee.id, year, month)
        system_config = get_system_config()

        late_days = attendance[5]
        early_leave_days = attendance[6]
        leave_days = attendance[7]
        overtime_hours = attendance[8]

        # 计算扣款
        deductions = (late_days * system_config['late_deduction_rate']) + \
                     (early_leave_days * system_config['early_leave_deduction_rate'])

        # 请假天数的处理，假设最大允许3天
        max_leave_days = 3
        if leave_days > max_leave_days:
            extra_leave_days = leave_days - max_leave_days
            deductions += extra_leave_days * system_config['late_deduction_rate']

        # 计算加班费
        overtime_rate = system_config['overtime_bonus_rate']
        overtime_bonus = overtime_hours * overtime_rate  # 加班费 = 加班小时数 * 加班时薪

        # 计算应发工资和实发工资
        gross_salary = base_salary + housing_allowance + overtime_bonus
        net_salary = gross_salary - deductions

        cleaned_data['gross_salary'] = gross_salary
        cleaned_data['deductions'] = deductions
        cleaned_data['net_salary'] = net_salary

        return cleaned_data


@login_required
@user_passes_test(is_admin)
def salary_list(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT es.id, es.year, es.month, es.employee_id, es.department_id, es.base_salary, 
                   es.housing_allowance, es.gross_salary, es.deductions, es.net_salary,
                   e.name AS employee_name, d.name AS department_name
            FROM employee_salary es
            JOIN employee_employee e ON es.employee_id = e.id
            JOIN employee_department d ON es.department_id = d.id
        """)
        salaries = cursor.fetchall()

    system_config = get_system_config()

    return render(request, 'salary_list.html', {
        'salaries': salaries,
        'system_config': system_config
    })




@login_required
@user_passes_test(is_admin)
def salary_add(request):
    if request.method == "GET":
        form = SalaryModelForm()
        return render(request, 'salary_add.html', {"form": form})

    form = SalaryModelForm(data=request.POST)
    if form.is_valid():
        # 保存记录
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO employee_salary (year, month, employee_id, department_id, base_salary, 
                housing_allowance, gross_salary, deductions, net_salary)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            [
                form.cleaned_data['year'],
                form.cleaned_data['month'],
                form.cleaned_data['employee'].id,
                form.cleaned_data['department'].id,
                form.cleaned_data['base_salary'],
                form.cleaned_data['housing_allowance'],
                form.cleaned_data['gross_salary'],
                form.cleaned_data['deductions'],
                form.cleaned_data['net_salary'],
                           ])

        return redirect('/salary/list/')

    # 如果表单无效，直接返回
    return render(request, 'salary_add.html', {"form": form})



@login_required
@user_passes_test(is_admin)
def salary_edit(request, nid):
    if request.method == "GET":
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT es.id, es.year, es.month, es.employee_id, es.department_id, es.base_salary, 
                       es.housing_allowance, es.gross_salary, es.deductions, es.net_salary,
                       e.name AS employee_name, d.name AS department_name
                FROM employee_salary es
                LEFT JOIN employee_employee e ON es.employee_id = e.id
                LEFT JOIN employee_department d ON es.department_id = d.id
                WHERE es.id = %s
            """, [nid])
            row = cursor.fetchone()

        if not row:
            return redirect('/salary/list/')  # 如果没有找到该记录，跳转到列表页面

        initial_data = {
            'id': row[0],
            'year': row[1],
            'month': row[2],
            'employee': row[3],
            'department': row[4],
            'base_salary': row[5],
            'housing_allowance': row[6],
            'gross_salary': row[7],
            'deductions': row[8],
            'net_salary': row[9]
        }

        form = SalaryModelForm(initial=initial_data)
        return render(request, 'salary_edit.html', {"form": form})

    form = SalaryModelForm(data=request.POST)
    if form.is_valid():
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE employee_salary
                SET year = %s, month = %s, employee_id = %s, department_id = %s, 
                    base_salary = %s, housing_allowance = %s, gross_salary = %s,
                    deductions = %s, net_salary = %s
                WHERE id = %s
            """, [
                form.cleaned_data['year'],
                form.cleaned_data['month'],
                form.cleaned_data['employee'].id,
                form.cleaned_data['department'].id,
                form.cleaned_data['base_salary'],
                form.cleaned_data['housing_allowance'],
                form.cleaned_data['gross_salary'],
                form.cleaned_data['deductions'],
                form.cleaned_data['net_salary'],
                nid
            ])
        return redirect('/salary/list/')

    return render(request, 'salary_edit.html', {"form": form})





@login_required
@user_passes_test(is_admin)
def salary_delete(request, nid):
    with connection.cursor() as cursor:
        cursor.execute("""
            DELETE FROM employee_salary WHERE id = %s
        """, [nid])

    return redirect('/salary/list/')


@login_required
@user_passes_test(is_admin)
def salary_search(request):
    search_query = request.GET.get('search', '')
    year_query = request.GET.get('year', '')
    month_query = request.GET.get('month', '')
    employee_query = request.GET.get('employee', '')
    department_query = request.GET.get('department', '')

    query = '''
     SELECT es.id, es.year, es.month, es.employee_id, es.department_id, es.base_salary, 
                   es.housing_allowance, es.gross_salary, es.deductions, es.net_salary,
                   e.name AS employee_name, d.name AS department_name
            FROM employee_salary es
            JOIN employee_employee e ON es.employee_id = e.id
            JOIN employee_department d ON es.department_id = d.id
            WHERE 1=1
            '''
    params = []

    if search_query:
        query += " AND e.name LIKE %s"
        params.append(f"%{search_query}%")

    if year_query:
        query += " AND es.year = %s"
        params.append(year_query)

    if month_query:
        query += " AND es.month = %s"
        params.append(month_query)

    if employee_query:
        query += " AND e.name LIKE %s"
        params.append(f"%{employee_query}%")

    if department_query:
        query += " AND d.name LIKE %s"
        params.append(f"%{department_query}%")

    with connection.cursor() as cursor:
        cursor.execute(query, params)
        salaries = cursor.fetchall()

    return render(request, 'salary_list.html', {
        'salaries': salaries,
        'search_query': search_query,
        'year_query': year_query,
        'month_query': month_query,
        'employee_query': employee_query,
        'department_query': department_query
    })


class configModelForm(forms.ModelForm):
    class Meta:
        model = models.EmployeeSystemconfig
        fields = ["id", "work_days_per_month", "late_deduction_rate", "early_leave_deduction_rate",
                  "leave_deduction_rate", "overtime_bonus_rate"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name != 'id':
                field.widget.attrs = {"class": "form-control"}



@login_required
@user_passes_test(is_admin)
def config_edit(request):
    # 使用 SQL 获取系统配置
    system_config = get_system_config()

    if request.method == "GET":
        # 创建表单并填充系统配置数据
        form = configModelForm(initial={
            'id': system_config['id'],
            'work_days_per_month': system_config['work_days_per_month'],
            'late_deduction_rate': system_config['late_deduction_rate'],
            'early_leave_deduction_rate': system_config['early_leave_deduction_rate'],
            'leave_deduction_rate': system_config['leave_deduction_rate'],
            'overtime_bonus_rate': system_config['overtime_bonus_rate'],
        })
        return render(request, 'config_edit.html', {"form": form})

    form = configModelForm(data=request.POST)
    if form.is_valid():
        # 获取表单提交的配置数据
        work_days_per_month = form.cleaned_data['work_days_per_month']
        late_deduction_rate = form.cleaned_data['late_deduction_rate']
        early_leave_deduction_rate = form.cleaned_data['early_leave_deduction_rate']
        leave_deduction_rate = form.cleaned_data['leave_deduction_rate']
        overtime_bonus_rate = form.cleaned_data['overtime_bonus_rate']

        # 使用 SQL 更新配置
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE employee_systemconfig
                SET work_days_per_month = %s,
                    late_deduction_rate = %s,
                    early_leave_deduction_rate = %s,
                    leave_deduction_rate = %s,
                    overtime_bonus_rate = %s
                WHERE id = %s
            """, [
                work_days_per_month,
                late_deduction_rate,
                early_leave_deduction_rate,
                leave_deduction_rate,
                overtime_bonus_rate,
                system_config['id']
            ])

        # 重新计算并更新所有员工薪资
        # update_all_salaries() 这里加注释是因为采用触发器替代了这个函数的功能

        return redirect('/salary/list/')

    return render(request, 'config_edit.html', {"form": form})

def update_all_salaries():
    # 获取最新的薪资配置
    system_config = get_system_config()

    # 遍历所有员工薪资记录并重新计算
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, employee_id, year, month, base_salary, housing_allowance
            FROM employee_salary
        """)
        salaries = cursor.fetchall()

    for salary in salaries:
        employee_id = salary[1]
        year = salary[2]
        month = salary[3]
        base_salary = salary[4]
        housing_allowance = salary[5]

        # 重新计算薪资
        gross_salary, deductions, net_salary = calculate_salary(employee_id, year, month, base_salary, housing_allowance)

        # 更新计算后的薪资
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE employee_salary
                SET gross_salary = %s, deductions = %s, net_salary = %s
                WHERE id = %s
            """, [gross_salary, deductions, net_salary, salary[0]])


@login_required
@user_passes_test(lambda u: u.is_superuser)
def department_salary_summary(request):
    """统计各部门薪资分配情况"""
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM department_salary_summary")
        result = cursor.fetchall()

    # 将结果转换为字典
    summary = []
    for row in result:
        summary.append({
            "department_name": row[0],
            "total_base_salary": row[1],
            "total_housing_allowance": row[2],
            "total_gross_salary": row[3],
            "total_deductions": row[4],
            "total_net_salary": row[5],
        })

    return render(request, 'department_salary_summary.html', {"summary": summary})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def department_salary_chart(request):
    """渲染部门薪资分配的饼图页面"""
    with connection.cursor() as cursor:
        cursor.execute("SELECT department_name, SUM(total_net_salary) FROM department_salary_summary GROUP BY department_name")
        result = cursor.fetchall()

    labels = [row[0] for row in result]
    values = [row[1] for row in result]

    return render(request, 'department_salary_chart.html', {
        'labels': labels,
        'values': values
    })