from rest_framework import viewsets

from .models import FieldType
from .serializer import FieldTypeSerializer

class FieldTypesViewSet(viewsets.ModelViewSet):
    """ This viewset automatically provides `list` and `detail` actions. """

    queryset = FieldType.objects.all()
    serializer_class = FieldTypeSerializer
