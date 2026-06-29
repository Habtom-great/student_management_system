from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from apps.accounts import views as account_views

urlpatterns = [
    # HOME
    path('', account_views.home, name='home'),

    # ADMIN
    path('admin/', admin.site.urls),

    # APPS
    path('accounts/', include('apps.accounts.urls')),
    path('students/', include('apps.students.urls')),
    path('courses/', include('apps.courses.urls')),
    path('exams/', include('apps.exams.urls')),
    path('payments/', include('apps.payments.urls')),
    path('instructors/', include('apps.instructors.urls')),
]

# MEDIA + STATIC (DEV ONLY)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)