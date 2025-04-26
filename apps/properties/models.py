from django.db import models
from apps.users.models import CustomUser

class Property(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=100)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='properties')

    def __str__(self):
        return f"{self.name} - {self.city}"
