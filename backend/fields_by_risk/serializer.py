from .models import FieldByRisk
from rest_framework import serializers

class FieldByRiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldByRisk
        fields =  '__all__'
