from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrOwner(BasePermission):
    """
    Seuls les admins peuvent tout voir,
    les propriétaires ne voient que leurs propres biens
    """
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.role == 'admin':
            return True
        return obj.owner == user
