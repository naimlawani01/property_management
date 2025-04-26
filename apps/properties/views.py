from rest_framework import viewsets
from .models import Property
from .serializers import PropertySerializer
from .permissions import IsAdminOrOwner
from rest_framework.permissions import IsAuthenticated

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated, IsAdminOrOwner]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Property.objects.all()
        elif user.role == 'owner':
            return Property.objects.filter(owner=user)
        return Property.objects.none()
