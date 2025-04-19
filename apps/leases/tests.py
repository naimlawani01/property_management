from django.test import TestCase

from django.contrib.auth.models import User
from rest_framework.test import APIClient # type: ignore
from rest_framework import status # type: ignore
from .models import Lease, Bien, Locataire

class LeaseAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        
        self.bien = Bien.objects.create(nom="Appartement", adresse="Dakar")
        self.locataire = Locataire.objects.create(nom="Sekou Sylla", email="sekou@example.com")

        self.lease_data = {
            "bien": self.bien.id,
            "locataire": self.locataire.id,
            "date_debut": "2025-04-01",
            "date_fin": "2025-10-01",
            "loyer": 500000,
            "statut_contrat": "actif"
        }

    def test_create_lease(self):
        response = self.client.post('/leases/', self.lease_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_lease_list(self):
        response = self.client.get('/leases/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_lease(self):
        lease = Lease.objects.create(**self.lease_data)
        update_data = {"loyer": 600000}
        response = self.client.patch(f'/leases/{lease.id}/', update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_lease(self):
        lease = Lease.objects.create(**self.lease_data)
        response = self.client.delete(f'/leases/{lease.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

