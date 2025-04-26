from rest_framework import serializers

from apps.leases.serializers import LeaseSerializer
from .models import Payment
from apps.leases.models import Lease

class PaymentSerializer(serializers.ModelSerializer):
    lease = LeaseSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = ['id', 'lease', 'date', 'amount', 'method', 'status']
