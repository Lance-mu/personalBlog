from django.shortcuts import render
from django.http import HttpResponse

from user.models import User

# Create your views here.


def home(request):
    return HttpResponse('这是首页的页面')


def login(request):
    request.POST
    return render(request, "login.html")


# 构建了一个视图样例--> 添加用户数据
def create_user(request):
    user = User()
    user.username = request.POST["username"]
    user. password = request.POST["password"]
    # user.create_time = '2022-01-12 23:51'
    user.save()

    return HttpResponse("创建用户成功")

    # create_time

