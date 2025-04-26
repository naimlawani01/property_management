from rest_framework import viewsets
from .models import Lease
from .serializers import LeaseSerializer
from .permissions import IsAdminOrLeaseParticipant
from rest_framework.permissions import IsAuthenticated

class LeaseViewSet(viewsets.ModelViewSet):
    queryset = Lease.objects.all()
    serializer_class = LeaseSerializer
    permission_classes = [IsAuthenticated, IsAdminOrLeaseParticipant]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Lease.objects.all()
        elif user.role == 'owner':
            return Lease.objects.filter(property__owner=user)
        elif user.role == 'tenant':
            return Lease.objects.filter(tenant=user)
        return Lease.objects.none()
