from django.db import models
from apps.leases.models import Lease

class Payment(models.Model):
    lease = models.ForeignKey(Lease, on_delete=models.CASCADE, related_name='payments')
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=50, choices=[('cash', 'Cash'), ('bank', 'Bank Transfer'), ('card', 'Card')])
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('paid', 'Paid')])

    def __str__(self):
        return f"{self.lease} - {self.amount}€ - {self.status}"
