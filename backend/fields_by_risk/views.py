from rest_framework import viewsets

from .models import FieldByRisk
from .serializer import FieldByRiskSerializer

class FieldByRiskViewSet(viewsets.ModelViewSet):
    """ This viewset automatically provides `list` and `detail` FieldByRisk actions. """

    queryset = FieldByRisk.objects.all()
    serializer_class = FieldByRiskSerializer
