from rest_framework import generics

from .models import Field
from .serializer import FieldSerializer

class FieldList(generics.ListCreateAPIView):
    """ List all fields, or create a new field """

    queryset = Field.objects.all()
    serializer_class = FieldSerializer

class FieldDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Retrieve, update or delete a field instance """

    queryset = Field.objects.all()
    serializer_class = FieldSerializer
