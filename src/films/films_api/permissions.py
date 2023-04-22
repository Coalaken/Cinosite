from rest_framework import permissions


class IsOwnerOrStaffOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(
            request.user.is_authentecated and 
            obj.added_by == request.user or 
            request.user.is_authentecated and
            request.user.is_staff
        )