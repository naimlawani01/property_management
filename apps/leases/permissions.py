from rest_framework.permissions import BasePermission

class IsAdminOrLeaseParticipant(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.role == 'admin':
            return True
        if user.role == 'owner':
            return obj.property.owner == user
        if user.role == 'tenant':
            return obj.tenant == user
        return False
