from .models import RiskType
from rest_framework import serializers

# class RiskTypeSerializer(serializers.HyperlinkedModelSerializer):
class RiskTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskType
        fields =  '__all__'
