# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class EmployeeAttendance(models.Model):
    year = models.IntegerField(verbose_name="年份")
    month = models.IntegerField(verbose_name="月份")
    employee = models.ForeignKey('EmployeeEmployee', models.DO_NOTHING,verbose_name="姓名", blank=True, null=True)
    department = models.ForeignKey('EmployeeDepartment', models.DO_NOTHING, verbose_name="部门",blank=True, null=True)
    late_days = models.IntegerField(verbose_name="迟到天数",blank=True, null=True)
    early_leave_days = models.IntegerField(verbose_name="早退天数",blank=True, null=True)
    leave_days = models.IntegerField(verbose_name="请假天数",blank=True, null=True)
    overtime_hours = models.FloatField(verbose_name="加班时长",blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'employee_attendance'


class EmployeeDepartment(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'employee_department'
    def __str__(self):
        return self.name

class EmployeeEmployee(models.Model):
    name = models.CharField(verbose_name="姓名",max_length=3)
    supervisor = models.ForeignKey('self', models.DO_NOTHING, verbose_name="上级",blank=True, null=True)
    department = models.ForeignKey(EmployeeDepartment, models.DO_NOTHING, verbose_name="部门",blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'employee_employee'

    def __str__(self):
        return self.name


class EmployeeSalary(models.Model):
    year = models.IntegerField(verbose_name="年份")
    month = models.IntegerField(verbose_name="月份")
    employee = models.ForeignKey(EmployeeEmployee, models.DO_NOTHING,verbose_name="姓名", blank=True, null=True)
    department = models.ForeignKey(EmployeeDepartment, models.DO_NOTHING, verbose_name="部门",blank=True, null=True)
    base_salary = models.FloatField(verbose_name="基础薪资",blank=True, null=True)
    housing_allowance = models.FloatField(verbose_name="住房补贴",blank=True, null=True)
    gross_salary = models.FloatField(verbose_name="应发金额",blank=True, null=True)
    deductions = models.FloatField(verbose_name="应扣金额",blank=True, null=True)
    net_salary = models.FloatField(verbose_name="实发金额",blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'employee_salary'

    

class EmployeeSystemconfig(models.Model):
    work_days_per_month = models.IntegerField(verbose_name="每月工作天数",blank=True, null=True)
    late_deduction_rate = models.FloatField(verbose_name="迟到扣款",blank=True, null=True)
    early_leave_deduction_rate = models.FloatField(verbose_name="早退扣款",blank=True, null=True)
    leave_deduction_rate = models.FloatField(verbose_name="请假超过规定扣款",blank=True, null=True)
    overtime_bonus_rate = models.FloatField(verbose_name="加班补贴",blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'employee_systemconfig'
