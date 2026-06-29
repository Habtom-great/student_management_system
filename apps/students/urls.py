from django.urls import path
from . import views

app_name = "students"

urlpatterns = [
    # /students/
    path("", views.student_list, name="student_home"),
     # /dashboard/
     
     path('students_dashboard/', views.students_dashboard, name='students_dashboard'),
    # /students/list/
    path("list/", views.student_list, name="student_list"),

    # /students/add/
    path("add/", views.add_student, name="add_student"),

    # /students/edit/1/
    path("edit/<int:student_id>/", views.edit_student, name="edit_student"),

    # /students/delete/1/
    path("delete/<int:student_id>/", views.delete_student, name="delete_student"),
]
