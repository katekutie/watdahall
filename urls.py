from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('userprofile', views.userprofile, name="userprofile"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('tips', views.tips, name="tips"),
    path('landingpage', views.landingpage, name="landingpage"),
]