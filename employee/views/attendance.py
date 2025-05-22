from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django import forms
from employee import models
from django.db import connection

# 检查是否为管理员
def is_admin(user):
    return user.is_superuser

# 出勤列表
@login_required
def attendance_list(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                a.id, a.year, a.month, e.name AS employee_name, 
                d.name AS department_name, a.late_days, 
                a.early_leave_days, a.leave_days, a.overtime_hours
            FROM employee_attendance a
            LEFT JOIN employee_employee e ON a.employee_id = e.id
            LEFT JOIN employee_department d ON a.department_id = d.id
        """)
        queryset = cursor.fetchall()

    return render(request, 'attendance_list.html', {"queryset": queryset})

# 出勤表的 ModelForm
class AttModelForm(forms.ModelForm):
    class Meta:
        model = models.EmployeeAttendance
        fields = ["id", "year", "month", "employee", "department", "late_days", "early_leave_days", "leave_days", "overtime_hours"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control"}

# 添加出勤记录
@login_required
@user_passes_test(is_admin)
def attendance_add(request):
    if request.method == "GET":
        form = AttModelForm()
        return render(request, 'attendance_add.html', {"form": form})

    form = AttModelForm(data=request.POST)
    if form.is_valid():
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO employee_attendance (year, month, employee_id, department_id, late_days, early_leave_days, leave_days, overtime_hours)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, [
                form.cleaned_data['year'],
                form.cleaned_data['month'],
                form.cleaned_data['employee'].id,
                form.cleaned_data['department'].id,
                form.cleaned_data['late_days'],
                form.cleaned_data['early_leave_days'],
                form.cleaned_data['leave_days'],
                form.cleaned_data['overtime_hours']
            ])
        return redirect('/attendance/list/')

    return render(request, 'attendance_add.html', {"form": form})

# 编辑出勤记录
@login_required
@user_passes_test(is_admin)
def attendance_edit(request, nid):
    if request.method == "GET":
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id, year, month, employee_id, department_id, late_days, early_leave_days, leave_days, overtime_hours
                FROM employee_attendance WHERE id = %s
            """, [nid])
            row = cursor.fetchone()

        if not row:
            return redirect('/attendance/list/')

        initial_data = {
            'id': row[0],
            'year': row[1],
            'month': row[2],
            'employee': row[3],
            'department': row[4],
            'late_days': row[5],
            'early_leave_days': row[6],
            'leave_days': row[7],
            'overtime_hours': row[8]
        }
        form = AttModelForm(initial=initial_data)
        return render(request, 'attendance_edit.html', {"form": form})

    form = AttModelForm(data=request.POST)
    if form.is_valid():
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE employee_attendance
                SET year = %s, month = %s, employee_id = %s, department_id = %s, 
                    late_days = %s, early_leave_days = %s, leave_days = %s, overtime_hours = %s
                WHERE id = %s
            """, [
                form.cleaned_data['year'],
                form.cleaned_data['month'],
                form.cleaned_data['employee'].id,
                form.cleaned_data['department'].id,
                form.cleaned_data['late_days'],
                form.cleaned_data['early_leave_days'],
                form.cleaned_data['leave_days'],
                form.cleaned_data['overtime_hours'],
                nid
            ])
        return redirect('/attendance/list/')

    return render(request, 'attendance_edit.html', {"form": form})

# 删除出勤记录
@login_required
@user_passes_test(is_admin)
def attendance_delete(request, nid):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM employee_attendance WHERE id = %s", [nid])
    return redirect('/attendance/list/')

# 出勤记录搜索
@login_required
def attendance_search(request):
    search_query = request.GET.get('search', '').strip()
    year_query = request.GET.get('year', '').strip()
    month_query = request.GET.get('month', '').strip()
    employee_query = request.GET.get('employee', '').strip()
    department_query = request.GET.get('department', '').strip()

    query = """
        SELECT 
            a.id, a.year, a.month, e.name AS employee_name, 
            d.name AS department_name, a.late_days, 
            a.early_leave_days, a.leave_days, a.overtime_hours
        FROM employee_attendance a
        LEFT JOIN employee_employee e ON a.employee_id = e.id
        LEFT JOIN employee_department d ON a.department_id = d.id
        WHERE 1=1
    """
    params = []

    if search_query:
        query += " AND e.name LIKE %s"
        params.append(f"%{search_query}%")

    if year_query:
        query += " AND a.year = %s"
        params.append(year_query)

    if month_query:
        query += " AND a.month = %s"
        params.append(month_query)

    if employee_query:
        query += " AND e.name LIKE %s"
        params.append(f"%{employee_query}%")

    if department_query:
        query += " AND d.name LIKE %s"
        params.append(f"%{department_query}%")

    with connection.cursor() as cursor:
        cursor.execute(query, params)
        queryset = cursor.fetchall()

    return render(request, 'attendance_list.html', {
        'queryset': queryset,
        'search_query': search_query,
        'year_query': year_query,
        'month_query': month_query,
        'employee_query': employee_query,
        'department_query': department_query
    })
