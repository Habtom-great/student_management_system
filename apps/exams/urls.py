from django.urls import path
from . import views

app_name = "exams"

urlpatterns = [
    path("", views.exam_dashboard, name="home"),
    path("dashboard/", views.exams_dashboard, name="exams_dashboard"),
    path("add/", views.add_exams, name="add_exams"),
    path("edit/<int:exam_id>/", views.edit_exams, name="edit_exams"),
    path("delete/<int:exam_id>/", views.delete_exams, name="delete_exams"),
]