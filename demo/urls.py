"""
URL configuration for demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from employee.views import depart,user,attendance,login,salary,index,super
from django.shortcuts import redirect

urlpatterns = [
    # path('', lambda request: redirect('login')),
    path('', index.index),
    path("admin/", admin.site.urls),

    #部门管理
    path("depart/list/", depart.depart_list),
    path("depart/add/", depart.depart_add),
    path("depart/delete/", depart.depart_delete),
    path("depart/<int:nid>/edit/", depart.depart_edit),
    path("depart/search/", depart.depart_search, name="depart_search"),

    #用户管理
    path("user/list/", user.user_list),
    path("user/add/", user.user_add),
    path("user/<int:nid>/edit/", user.user_edit),
    path("user/<int:nid>/delete/", user.user_delete),
    path("user/<int:nid>/attendance_salary/", user.user_attendance_salary),
    path("user/search/", user.user_search, name="user_search"),

    #出勤管理
    path("attendance/list/", attendance.attendance_list),
    path("attendance/add/", attendance.attendance_add),
    path("attendance/<int:nid>/edit/", attendance.attendance_edit),
    path("attendance/<int:nid>/delete/", attendance.attendance_delete),
    path("attendance/search/", attendance.attendance_search, name="attendance_search"),  # 新增查询路径

    #登录注销
    path('login/', login.user_login, name='login'),
    path('register/', login.register, name='register'),
    path('logout/', login.user_logout, name='logout'),

    #薪资界面
    path("salary/list/", salary.salary_list),
    path("salary/add/", salary.salary_add),
    path("salary/<int:nid>/edit/", salary.salary_edit),
    path("salary/<int:nid>/delete/", salary.salary_delete),
    path("config/edit/", salary.config_edit),
    path("salary/search/", salary.salary_search, name="salary_search"),



    path('super_list/', super.user_list, name='user_list'),
    # 修改用户管理员身份的视图
    path('modify_user_admin/<int:user_id>/', super.modify_user_admin_status, name='modify_user_admin_status'),
    # 删除用户的视图
    path('delete_user/<int:user_id>/', super.delete_user, name='delete_user'),


    path('salary/summary/', salary.department_salary_summary, name='department_salary_summary'),
    path('salary/chart/', salary.department_salary_chart, name='department_salary_chart'),
]
