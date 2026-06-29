from django.urls import path
from . import views

app_name = "instructors"

urlpatterns = [
    path("", views.instructor_list, name="list"),
    path("add/", views.add_instructor, name="add"), 
    path("<int:pk>/", views.instructor_detail, name="detail"),
    path("<int:pk>/edit/", views.edit_instructor, name="edit"),
    path("<int:pk>/delete/", views.delete_instructor, name="delete"),
]