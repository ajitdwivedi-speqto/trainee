from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission:
    - Staff users (is_staff=True) can do anything (GET, POST, PUT, PATCH, DELETE).
    - Non-staff users can only read (GET, HEAD, OPTIONS).
    """
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return request.method in SAFE_METHODS
