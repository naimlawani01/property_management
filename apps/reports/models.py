from django.db import models
from apps.properties.models import Property

class Report(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='reports')
    date_generated = models.DateTimeField(auto_now_add=True)
    summary = models.TextField()
    total_rent_collected = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Report for {self.property.name} - {self.date_generated.strftime('%Y-%m-%d')}"
