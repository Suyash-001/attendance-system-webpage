from django.contrib import admin
from django.urls import path, include
from homepage import views

urlpatterns = [
    path('', views.ind, name='home')
    
]
