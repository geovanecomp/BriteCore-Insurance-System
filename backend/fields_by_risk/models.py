from django.db import models
from fields.models import Field
from risks.models import Risk

class FieldByRisk(models.Model):
    """ Defines all fields by risk """
    field = models.ForeignKey(Field, null=False, on_delete=models.CASCADE)
    risk = models.ForeignKey(Risk, null=False, on_delete=models.CASCADE)
    value = models.CharField(max_length=100, null=False)
