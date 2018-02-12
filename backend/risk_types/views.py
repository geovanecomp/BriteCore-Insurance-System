from rest_framework import generics

from .models import RiskType
from .serializer import RiskTypeSerializer

class RiskTypeList(generics.ListCreateAPIView):
    """ List all risk types, or create a new risk type"""

    queryset = RiskType.objects.all()
    serializer_class = RiskTypeSerializer


class RiskTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Retrieve, update or delete a risk type instance """

    queryset = RiskType.objects.all()
    serializer_class = RiskTypeSerializer
