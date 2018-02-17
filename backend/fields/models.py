from django.db import models
from field_types.models import FieldType

class Field(models.Model):
    """ Defines all fields """
    field_type = models.ForeignKey(FieldType, null=False, on_delete=models.CASCADE)
    label = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=255, null=True)
    required = models.NullBooleanField()

    def __repr__(self):
        return self.label + ' is added.'
