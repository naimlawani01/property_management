from rest_framework import serializers

from apps.properties.serializers import PropertySerializer
from .models import Report

class ReportSerializer(serializers.ModelSerializer):
    property = PropertySerializer(read_only=True)

    class Meta:
        model = Report
        fields = ['id', 'property', 'date_generated', 'summary', 'total_rent_collected']
