from django.contrib import admin
from django.urls import path, include
from apps.dashboard import views as dashboard_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # HOME
    path('', dashboard_views.home, name='home'),

    # APPS
    path('accounts/', include('apps.accounts.urls')),
    path('students/', include('apps.students.urls')),
    path('courses/', include('apps.courses.urls')),
    path('exams/', include('apps.exams.urls')),
    path('payments/', include('apps.payments.urls')),

    # DASHBOARD
    path('dashboard/admin/', dashboard_views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/instructor/', dashboard_views.instructor_dashboard, name='instructor_dashboard'),
    path('dashboard/student/', dashboard_views.student_dashboard, name='student_dashboard'),
]


