from rest_framework import viewsets

from .models import Risk
from .serializer import RiskSerializer

class RiskViewSet(viewsets.ModelViewSet):
    """ This viewset automatically provides `list` and `detail` actions for risks. """

    queryset = Risk.objects.all()
    serializer_class = RiskSerializer
