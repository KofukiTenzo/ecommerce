from rest_framework.permissions import BasePermission

class isManagerOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.group == "manager" | request.user.group == "admin"

    def has_object_permission(self, request, view, obj):
        return request.user.group == "manager" | request.user.group == "admin"