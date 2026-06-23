from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views  # Ensure your views are imported

app_name = 'courses'

urlpatterns = [
    # ------------------
    # Courses Dashboard / Listing
    # ------------------
    path('dashboard/', views.courses_dashboard, name='courses/courses_dashboard'),
    path('', views.course_list, name='courses/course_list'),

    # ------------------
    # Course Management
    # ------------------
    path('add/', views.add_course, name='add_course'),
    path('manage/', views.manage_courses, name='manage_courses'),
    path('<str:course_id>/view/', views.course_view, name='view_course'),
    path('<int:pk>/', views.course_detail, name='course_detail'),
    path('<str:course_id>/edit/', views.edit_course, name='edit_course'),
    path('<str:course_id>/delete/', views.delete_course, name='delete_course'),

    # ------------------
    # Static Pages (Optional)
    # ------------------
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
