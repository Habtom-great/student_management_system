# project/urls.py
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views
from . import forms
from .models import Payment

 # important to set app_name for namespa

app_name = 'payments'  # define namespace for the payments app

urlpatterns = [
   
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/', views.payments_dashboard, name='payments_dashboard'),
]

   