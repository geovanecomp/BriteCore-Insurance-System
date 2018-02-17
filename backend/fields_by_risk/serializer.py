from .models import FieldByRisk
from rest_framework import serializers
from risks.serializer import RiskSerializer
from fields.serializer import FieldSerializer

class FieldByRiskSerializer(serializers.ModelSerializer):
    field = FieldSerializer(read_only=True)
    risk = RiskSerializer(read_only=True)

    class Meta:
        model = FieldByRisk
        fields =  '__all__'
