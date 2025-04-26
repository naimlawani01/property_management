from rest_framework import serializers

from apps.properties.serializers import PropertySerializer
from .models import Lease
from apps.properties.models import Property
from apps.users.models import CustomUser

class LeaseSerializer(serializers.ModelSerializer):
    property = PropertySerializer(read_only=True)
    tenant = serializers.SlugRelatedField(queryset=CustomUser.objects.all(), slug_field='username')

    class Meta:
        model = Lease
        fields = ['id', 'property', 'tenant', 'start_date', 'end_date', 'rent_amount', 'is_active']
