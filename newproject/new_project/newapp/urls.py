from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.demo, name='demo'),
    path('register', views.register, name='registration'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]