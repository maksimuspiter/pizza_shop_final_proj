from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if (
            request.user.is_superuser
            or request.method in permissions.SAFE_METHODS
            and request.user.is_authenticated
        ):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        return obj.customer.user == request.user
