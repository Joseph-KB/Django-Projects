from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect

from .forms import RegisterForm,LoginForm

from django.contrib.auth import get_user_model,authenticate,login,logout

from django.contrib import messages

# Create your views here.

def registaration(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("customer:login"))
    else:
        form = RegisterForm()

    return render(request,'customer/registration.html',{
        "form" : form,
        })


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            username = form['username']
            password=form['password']
            user= authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('home:home'))
            else:
                message='Try authenticating again'
                form=LoginForm()
                return render(request,"customer/login.html",{"form":form,"message":message})
    if request.user.is_authenticated:
        message = 'LoggedIn Already'
        messages.info(request,message)
        return redirect('home:home')
    form=LoginForm()
    return render(request,"customer/login.html",{"form":form})
        

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        message = 'Logged Out. Come back soon for innovations. An Empire are build by Great Emperor'
        messages.info(request,message)
        return redirect('home:home')
    # redirect goes and find the names from urlpatterns, but reverse needs path to be specified
    message = 'Already logged out'
    messages.info(request,message)
    return redirect('home:home')
    

print(get_user_model().objects.all())