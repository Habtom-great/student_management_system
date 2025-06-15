from django.contrib import admin
from .models import Student, Course, Payment, Exam

admin.site.site_header = "Student Management Admin"
admin.site.site_title = "StudentMgmt Portal"
admin.site.index_title = "Welcome to the Student Management Dashboard"

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['registration_number', 'first_name', 'middle_name', 'last_name', 'email', 'is_active']
    list_filter = ('is_active', 'course', 'gender')  # only if these exist on your model
    search_fields = ('first_name', 'last_name', 'email', 'registration_number')
    readonly_fields = ('registration_number',)
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'middle_name', 'last_name', 'dob', 'gender', 'photo')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'address', 'country')
        }),
        ('Academic Information', {
            'fields': ('registration_number', 'course', 'is_active', 'notes')
        }),
    )

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'duration_months', 'fee')
    search_fields = ('name', 'code')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('receipt_number', 'student', 'amount', 'payment_date', 'is_confirmed')
    list_filter = ('payment_method', 'is_confirmed')
    search_fields = ('receipt_number', 'student__first_name', 'student__last_name')
    date_hierarchy = 'payment_date'

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'exam_date', 'location')
    list_filter = ('course',)
    search_fields = ('name', 'course__name')
    date_hierarchy = 'exam_date'
