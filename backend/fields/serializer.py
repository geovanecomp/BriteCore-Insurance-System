from .models import Field
from rest_framework import serializers
from field_types.serializer import FieldTypeSerializer
class FieldSerializer(serializers.ModelSerializer):
    # field_type = serializers.PrimaryKeyRelatedField(read_only=True)
    # field_type = FieldTypeSerializer(read_only=True)

    class Meta:
        model = Field
        fields =  '__all__'
        # fields =  ('field_type', 'name', 'description', 'required')
