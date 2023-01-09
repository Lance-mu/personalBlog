from django.shortcuts import render

# Create your views here.


def view_user1(request):
    return render(request, "user1.html")

