from rest_framework.permissions import BasePermission

class IsOwnerOrAdmin(BasePermission):
    """
    Seul le propriétaire ou un administrateur peut accéder/modifier/supprimer.
    """

    def has_object_permission(self, request, view, obj):
        # Si l'utilisateur est admin => autorisé
        if request.user.role == 'admin':
            return True
        
        # Sinon, il ne peut toucher qu'à lui-même
        return obj == request.user
