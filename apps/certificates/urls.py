from django.urls import path
from . import views

urlpatterns = [
    path('', views.certificate_list, name='certificate_list'),
    path('issue/<int:student_id>/', views.issue_certificate, name='issue_certificate'),
]