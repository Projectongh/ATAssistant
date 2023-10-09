from django.shortcuts import render
from django.db import connection
from django.shortcuts import render
from .models import *
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request,'html_files/home.html')
    # return render(request, 'static/home.html', {"free": freecard})

def contactus(request):
    status=False
    if request.method=='POST':
        name=request.POST.get("name","")
        email=request.POST.get("email","")
        phone=request.POST.get("phone","")
        message=request.POST.get("message","")
        x=contactus(name=name,email=email,phone=phone,message=message)
        x.save
        status=True
    return render(request,'html_files/contactus.html',{'S':status})




