from rest_framework import serializers # type: ignore
from .models import Lease

class LeaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lease
        fields = '__all__'

    def validate(self, data):
        """ Vérifie que la date de début est bien avant la date de fin """
        if data['date_debut'] >= data['date_fin']:
            raise serializers.ValidationError("La date de début doit être avant la date de fin.")
        return data
