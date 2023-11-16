from django.shortcuts import render

# Create your views here.

def registaration(request):
    return render(request,'customer/registration.html')


def user_login(request):
    return render(request,'customer/login.html')