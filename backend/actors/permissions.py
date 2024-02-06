from rest_framework.permissions import BasePermission

class AuthorizationPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.authorization > 1