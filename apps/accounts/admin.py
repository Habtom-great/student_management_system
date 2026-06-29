from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):

    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ()  # empty for now
        }),
    )

    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')

admin.site.register(User, UserAdmin)