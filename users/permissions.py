from rest_framework.permissions import BasePermission

class IsAuthenticated(BasePermission):
    message = 'You`re not authorised!'
    
    def has_permission(self, request, view):
        return super()

    def has_object_permission(self, request, view, obj):
        return super()

class IsManagerOrAdmin(BasePermission):
    message = 'You`re don`t have permissions!'
    
    def has_permission(self, request, view):
        return request.user.group == "manager" or request.user.group == "admin"

    def has_object_permission(self, request, view, obj):
        return request.user.group == "manager" or request.user.group == "admin"