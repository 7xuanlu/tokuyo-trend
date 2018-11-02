from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html')),
    path('home', views.home, name='home'),
    #path('login', views.login, name='login'),
    #path('register', views.register, name='register'),
    #path('forgot-password', views.forgot_password, name='forgot-password'),
]
