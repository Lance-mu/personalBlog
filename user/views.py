from django.shortcuts import render
from django.http import HttpResponse

from user.models import User

# Create your views here.


def home(request):
    return HttpResponse(request,'首页')


def login(request):
    return render(request, "login.html")


def create_user(request):
    user = User()
    user.username = ''
    return render(request,)

