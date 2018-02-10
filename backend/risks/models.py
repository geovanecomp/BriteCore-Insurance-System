from django.db import models

# Create your models here.
class RiskType(models.Model):
    name = models.CharField(max_length=100, null=False)
