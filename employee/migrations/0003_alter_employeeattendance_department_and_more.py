# Generated by Django 5.1.3 on 2024-12-28 13:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employee", "0002_alter_employeeemployee_supervisor"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employeeattendance",
            name="department",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="employee.employeedepartment",
                verbose_name="部门",
            ),
        ),
        migrations.AlterField(
            model_name="employeeattendance",
            name="early_leave_days",
            field=models.IntegerField(blank=True, null=True, verbose_name="早退天数"),
        ),
        migrations.AlterField(
            model_name="employeeattendance",
            name="employee",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="employee.employeeemployee",
                verbose_name="姓名",
            ),
        ),
        migrations.AlterField(
            model_name="employeeattendance",
            name="late_days",
            field=models.IntegerField(blank=True, null=True, verbose_name="迟到天数"),
        ),
        migrations.AlterField(
            model_name="employeeattendance",
            name="leave_days",
            field=models.IntegerField(blank=True, null=True, verbose_name="请假天数"),
        ),
        migrations.AlterField(
            model_name="employeeattendance",
            name="month",
            field=models.IntegerField(verbose_name="月份"),
        ),
        migrations.AlterField(
            model_name="employeeattendance",
            name="overtime_hours",
            field=models.FloatField(blank=True, null=True, verbose_name="加班时长"),
        ),
        migrations.AlterField(
            model_name="employeeattendance",
            name="year",
            field=models.IntegerField(verbose_name="年份"),
        ),
        migrations.AlterField(
            model_name="employeeemployee",
            name="department",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="employee.employeedepartment",
                verbose_name="部门",
            ),
        ),
        migrations.AlterField(
            model_name="employeeemployee",
            name="name",
            field=models.CharField(max_length=3, verbose_name="姓名"),
        ),
        migrations.AlterField(
            model_name="employeeemployee",
            name="supervisor",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="employee.employeeemployee",
                verbose_name="上级",
            ),
        ),
        migrations.AlterField(
            model_name="employeesalary",
            name="base_salary",
            field=models.FloatField(blank=True, null=True, verbose_name="基础薪资"),
        ),
        migrations.AlterField(
            model_name="employeesalary",
            name="deductions",
            field=models.FloatField(blank=True, null=True, verbose_name="应扣金额"),
        ),
        migrations.AlterField(
            model_name="employeesalary",
            name="department",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="employee.employeedepartment",
                verbose_name="部门",
            ),
        ),
        migrations.AlterField(
            model_name="employeesalary",
            name="employee",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="employee.employeeemployee",
                verbose_name="姓名",
            ),
        ),
        migrations.AlterField(
            model_name="employeesalary",
            name="gross_salary",
            field=models.FloatField(blank=True, null=True, verbose_name="应发金额"),
        ),
        migrations.AlterField(
            model_name="employeesalary",
            name="housing_allowance",
            field=models.FloatField(blank=True, null=True, verbose_name="住房补贴"),
        ),
        migrations.AlterField(
            model_name="employeesalary",
            name="month",
            field=models.IntegerField(verbose_name="月份"),
        ),
        migrations.AlterField(
            model_name="employeesalary",
            name="net_salary",
            field=models.FloatField(blank=True, null=True, verbose_name="实发金额"),
        ),
        migrations.AlterField(
            model_name="employeesalary",
            name="year",
            field=models.IntegerField(verbose_name="年份"),
        ),
        migrations.AlterField(
            model_name="employeesystemconfig",
            name="early_leave_deduction_rate",
            field=models.FloatField(blank=True, null=True, verbose_name="早退扣款"),
        ),
        migrations.AlterField(
            model_name="employeesystemconfig",
            name="late_deduction_rate",
            field=models.FloatField(blank=True, null=True, verbose_name="迟到扣款"),
        ),
        migrations.AlterField(
            model_name="employeesystemconfig",
            name="leave_deduction_rate",
            field=models.FloatField(
                blank=True, null=True, verbose_name="请假超过规定扣款"
            ),
        ),
        migrations.AlterField(
            model_name="employeesystemconfig",
            name="overtime_bonus_rate",
            field=models.FloatField(blank=True, null=True, verbose_name="加班补贴"),
        ),
        migrations.AlterField(
            model_name="employeesystemconfig",
            name="work_days_per_month",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="每月工作天数"
            ),
        ),
    ]
