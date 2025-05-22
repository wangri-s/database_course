from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.utils import IntegrityError
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password  # 导入 check_password
from django.contrib.auth import login, get_user_model  # 导入 login 和 get_user_model
from django.db import connection
from django.contrib.auth.hashers import make_password

# 注册视图
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '注册成功！请登录。')
            return redirect('login')
        else:
            messages.error(request, '注册失败，请检查输入内容。')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


# 登录视图
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # 使用 SQL 查询验证用户
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT password FROM auth_user WHERE username = %s
            """, [username])
            row = cursor.fetchone()

            if row is not None:
                stored_password = row[0]
                if check_password(password, stored_password):  # 使用 check_password 来验证密码
                    # 获取用户对象
                    User = get_user_model()  # 获取当前项目中的用户模型
                    user = User.objects.get(username=username)

                    # 使用 Django 的登录方法，完成用户认证和会话设置
                    login(request, user)

                    return redirect('/')  # 登录成功，重定向到主页
                else:
                    messages.error(request, '用户名或密码错误。')
            else:
                messages.error(request, '用户名或密码错误。')

    return render(request, 'login.html')


def user_logout(request):
    # 使用 SQL 删除用户的会话
    with connection.cursor() as cursor:
        cursor.execute("""
            DELETE FROM django_session WHERE session_key = %s
        """, [request.session.session_key])

    return redirect('/')  # 登出后重定向到主页
