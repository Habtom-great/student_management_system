from django.urls import path
from . import views

app_name = "students"

urlpatterns = [

    path('', views.student_list, name='student_list'),

    path('dashboard/', views.student_dashboard, name='student_dashboard'),

    path('add/', views.add_student, name='add_student'),

    path('edit/<int:student_id>/', views.edit_student, name='edit_student'),

    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),

    path('view/<int:student_id>/', views.student_detail, name='student_detail'),

    path('export/excel/', views.export_excel, name='export_excel'),

    path('export/pdf/', views.export_pdf, name='export_pdf'),

]