from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    context={"message":"Hello Moto"}
    return render(request,"home/home.html",{'context': context})