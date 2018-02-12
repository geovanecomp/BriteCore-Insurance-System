from rest_framework import generics

from .models import FieldType
from .serializer import FieldTypeSerializer

class FieldTypeList(generics.ListCreateAPIView):
    """ List all field types, or create a new field type"""

    queryset = FieldType.objects.all()
    serializer_class = FieldTypeSerializer



class FieldTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Retrieve, update or delete a field type instance """

    queryset = FieldType.objects.all()
    serializer_class = FieldTypeSerializer
