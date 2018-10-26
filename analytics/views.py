from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request, 'analytics/homepage.html')

def login(request):
    return render(request, 'analytics/login.html')

def register(request):
    return render(request, 'analytics/register.html')

def forgot_password(request):
    return render(request, 'analytics/forgot-password.html')
