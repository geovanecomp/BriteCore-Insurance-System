from django.db import models

class FieldType(models.Model):
    """Defines all field types"""
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=255, null=True)

    def __repr__(self):
        return self.name + ' is added.'
