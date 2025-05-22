from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # 渲染主页模板
