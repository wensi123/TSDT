from django.shortcuts import render

def home_page(request):
    return render(request, "home.html")  # 渲染 home.html 模板并返回响应
