from django.contrib import admin
from .models import Course
# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    class CourseAdmin(admin.ModelAdmin):
     list_display = ('course_id', 'course_title', 'department', 'instructor', 'created_at')
    search_fields = ('title', 'instructor')
    list_filter = ('created_at',)
