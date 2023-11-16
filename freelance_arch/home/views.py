from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    value='hai'
    context={"hello":value}
    return render(request,"home/home.html",context=context)

def login(request):
    if request.method=="POST":
        form=request.post
        if form.is_valid():
            login()

    else:
        return render(request,'home/login.html')