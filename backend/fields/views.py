from rest_framework import viewsets

from .models import Field
from .serializer import FieldSerializer

class FieldViewSet(viewsets.ModelViewSet):
    """ This viewset automatically provides `list` and `detail` actions. """

    queryset = Field.objects.all()
    serializer_class = FieldSerializer
