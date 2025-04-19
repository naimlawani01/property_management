from django.db import models

class Bien(models.Model):
    name = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Locataire(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Lease(models.Model):
    STATUT_CHOICES = [
        ('actif', 'Actif'),
        ('expiré', 'Expiré'),
        ('résilié', 'Résilié'),
    ]

    bien = models.ForeignKey(Bien, on_delete=models.CASCADE, related_name='leases')
    locataire = models.ForeignKey(Locataire, on_delete=models.CASCADE, related_name='leases')
    date_debut = models.DateField()
    date_fin = models.DateField()
    loyer = models.DecimalField(max_digits=10, decimal_places=2)
    statut_contrat = models.CharField(max_length=20, choices=STATUT_CHOICES, default='actif')
    date_signature = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contrat {self.id} - {self.locataire} pour {self.bien}"
