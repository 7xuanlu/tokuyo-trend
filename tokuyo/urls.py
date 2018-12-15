"""tokuyo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from analytics import views

urlpatterns = [
    path('', views.home, name=''),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path("topic/massage/", views.topic_massage, name="topic_massage"),
    path("topic/fit_equipment/", views.topic_fit, name="topic_fit_equipment"),
    path("topic/rival/", views.topic_rival, name="topic_rival"),
    path("trend/", views.trend, name="trend"),
    path("traffic/", views.traffic, name="traffic"),
    path('api/google_trend/', views.search_kw, name='google_trend_api'),
    path('admin/', admin.site.urls),
]
