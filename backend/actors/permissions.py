from rest_framework.permissions import BasePermission

class AuthorizationPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        cmp = request.user.authorization or 0
        return cmp > 1