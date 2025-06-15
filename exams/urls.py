# project/urls.py
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from students.models import Student, Course, Payment, Exam  # ✅ correct
from . import views # import views from app folder
from django.contrib import admin
from django.urls import include

def home(request):
    return HttpResponse("<h1>Welcome to the Student Management System - SMS !</h1>")
# project/urls.py



urlpatterns = [
    path('admin/', admin.site.urls),
    path('exams/', include('exams.urls')),  # ✅ Make sure this is here
    path('dashboard/', include('students.urls')),  # if your dashboard lives in students app
    path('dashboard/', views.exams_dashboard, name='exams_dashboard'),
    path('exams/', views.exam_dashboard, name='exam_dashboard'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Home page route
    path('add/', views.add_exams, name='add_exams'),
    path('edit/<int:pk>/', views.edit_exams, name='edit_exams'),
    path('delete/<int:pk>/', views.delete_exams, name='delete_exams'),
 
]