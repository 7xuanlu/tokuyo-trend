from django.shortcuts import render
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, 'home.html')

#def login(request):
    #return render(request, 'analytics/login.html')

#def register(request):
    #return render(request, 'analytics/register.html')

#def forgot_password(request):
    #return render(request, 'analytics/forgot-password.html')
