from django.contrib import admin
from .models import Student, Payment


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "phone",
        "city",
        "status",
        "created_at",   # ✅ correct field
    )

    search_fields = ("first_name", "last_name", "email")

    list_filter = ("status", "city", "created_at")


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("student", "amount", "status", "date")
    list_filter = ("status", "date")
    search_fields = ("student__first_name", "student__last_name")