from django.contrib import admin
from .models import Role, CustomUser

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'role', 'description')
    search_fields = ('role',)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'role', 'is_staff', 'is_active')
    search_fields = ('email', 'role__name', 'phone', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_active', 'role')