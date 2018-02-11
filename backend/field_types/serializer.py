from .models import FieldType
from rest_framework import serializers

class FieldTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldType
        fields =  '__all__'
