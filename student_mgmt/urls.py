from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views
from students import views  # your main app views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication URLs: login, logout, password reset, etc.
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    # Home and dashboard
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('students/dashboard/', views.students_dashboard, name='students_dashboard'),
    path('exams/dashboard/', views.exams_dashboard, name='exams_dashboard'),
   

    # Include app URLs with namespaces
    path('students/', include(('students.urls', 'students'), namespace='students')),
    path('courses/', include(('courses.urls', 'courses'), namespace='courses')),
    path('exams/', include(('exams.urls', 'exams'), namespace='exams')),
    path('payments/', include(('payments.urls', 'payments'), namespace='payments')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
