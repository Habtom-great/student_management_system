from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from apps.accounts import views
 # admin_dashboard, admin_instructors, instructor_dashboard, student_dashboard

urlpatterns = [
    # Home page
    path('', views.home, name='home'),  # ✅ ROOT URL FIX
    # Admin
    path('admin/', admin.site.urls),

    # Authentication (ONLY via accounts app — clean design)
    path('accounts/', include('apps.accounts.urls')),

    # Core apps
    path('students/', include('apps.students.urls')),
    path('courses/', include('apps.courses.urls')),
    path('exams/', include('apps.exams.urls')),
    path('payments/', include('apps.payments.urls')),

    # Dashboard (project-level views)
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/admin/', views.admin_instructors, name='admin_instructors'),
    path('dashboard/instructors/', views.instructor_dashboard, name='instructor_dashboard'),
    path('dashboard/students/', views.student_dashboard, name='student_dashboard'),
]

# Static & media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

