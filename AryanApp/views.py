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
    return render(request,'html_files/contactus.html')



