from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'base.html')

def welcome(request):
    return render(request,'welcome.html')