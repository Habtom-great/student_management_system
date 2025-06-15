from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'courses'

urlpatterns = [
    # Admin Dashboard
    path('dashboard/', views.courses_dashboard, name='courses_dashboard'),

    # Course List and Details
    path('', views.course_list, name='courses_list'),
    path('list/', views.course_list, name='course_list'),
    path('<int:pk>/view/', views.course_view, name='view_course'),  # Detail page for individual course
    path('princ-of-accounting/', views.accounting_details, name='principles_accounting'),
    # Add, Edit, Delete Course
    path('add/', views.add_course, name='add_course'),
    path('edit/<int:course_id>/', views.edit_course, name='edit_course'),
    path('delete/<int:course_id>/', views.delete_course, name='delete_course'),

    # Additional custom course detail pages
    path('accounting-detail/', views.accounting_details, name='accounting_details'),
    path('web-detail/', views.web_detail, name='web_detail'),

    # Optional: edit and delete by pk
    path('<int:pk>/edit/', views.course_edit, name='course_edit'),
    path('<int:pk>/delete/', views.course_delete, name='course_delete'),
]

# Serve media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
