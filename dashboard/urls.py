from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),  # 👈 add this
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('instructor/', views.instructor_dashboard, name='instructor_dashboard'),
    path('student/', views.student_dashboard, name='student_dashboard'),
]