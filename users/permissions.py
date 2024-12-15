from rest_framework.permissions import BasePermission
from .models import Role

class IsAuthenticated(BasePermission):
    message = 'You not authorised!'
    
    def has_permission(self, request, view):
        return super()

    def has_object_permission(self, request, view, obj):
        return super()

class IsManagerOrAdmin(BasePermission):
    message = 'You don`t have permissions!'
    
    def is_manager_or_admin(self, user):
        return user.is_authenticated and user.role in Role.objects.filter(role__in=["manager", "admin"])
    
    def has_permission(self, request, view):
        return self.is_manager_or_admin(request.user)

    def has_object_permission(self, request, view, obj):
        return self.is_manager_or_admin(request.user)