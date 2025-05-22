from django.shortcuts import render, redirect
from django.db import connection
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

# 确保只有管理员可以访问
def is_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(is_admin)
def user_list(request):
    try:
        # 使用 SQL 查询获取所有用户
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, username, email, is_superuser FROM auth_user")
            users = cursor.fetchall()
    except Exception as e:
        messages.error(request, f"数据库查询错误: {e}")
        users = []

    return render(request, 'super_list.html', {'users': users})

@login_required
@user_passes_test(is_admin)
def modify_user_admin_status(request, user_id):
    try:
        with connection.cursor() as cursor:
            # 检查该用户是否存在
            cursor.execute("SELECT id, username, is_superuser FROM auth_user WHERE id = %s", [user_id])
            user = cursor.fetchone()

            if not user:
                messages.error(request, "用户不存在。")
                return redirect('user_list')

            # 切换用户是否为管理员
            if user[2]:  # 如果是超级管理员
                cursor.execute("UPDATE auth_user SET is_superuser = 0, is_staff = 0 WHERE id = %s", [user_id])
                messages.success(request, f"{user[1]} 已被撤销管理员权限。")
            else:
                cursor.execute("UPDATE auth_user SET is_superuser = 1, is_staff = 1 WHERE id = %s", [user_id])
                messages.success(request, f"{user[1]} 已被赋予管理员权限。")

            # 提交修改
            connection.commit()

    except Exception as e:
        messages.error(request, f"数据库错误: {e}")

    return redirect('user_list')  # 修改完权限后，重定向到用户列表页面

@login_required
@user_passes_test(is_admin)
def delete_user(request, user_id):
    try:
        with connection.cursor() as cursor:
            # 删除用户
            cursor.execute("DELETE FROM auth_user WHERE id = %s", [user_id])
            connection.commit()
            messages.success(request, f"用户已成功删除！")
    except Exception as e:
        messages.error(request, f"删除用户时出错: {e}")

    return redirect('user_list')  # 删除后重定向到用户列表页面

