from django.db import models
from risks.models import RiskType

class Risk(models.Model):
    """ Defines all risks """
    risk_type = models.ForeignKey(RiskType, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=255, null=True)

    def __repr__(self):
        return self.name + ' is added.'
