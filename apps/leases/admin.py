from django.contrib import admin
from .models import Lease

@admin.register(Lease)
class LeaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'locataire', 'bien', 'date_debut', 'date_fin', 'loyer', 'statut_contrat')
    list_filter = ('statut_contrat', 'date_debut', 'date_fin')
    search_fields = ('locataire__nom', 'bien__nom', 'statut_contrat')
    ordering = ('-date_signature',)

