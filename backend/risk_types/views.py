from rest_framework import viewsets

from .models import RiskType
from .serializer import RiskTypeSerializer

class RiskTypeViewSet(viewsets.ModelViewSet):
    """ This viewset automatically provides `list` and `detail` actions. """

    queryset = RiskType.objects.all()
    serializer_class = RiskTypeSerializer
