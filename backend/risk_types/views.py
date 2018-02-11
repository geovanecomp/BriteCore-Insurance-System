from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404

from .models import RiskType
from .serializer import RiskTypeSerializer

class RiskTypeList(APIView):
    """ List all risk types, or create a new risk type"""

    def get(self, request, format=None):
        risk_types = RiskType.objects.all()
        serializer = RiskTypeSerializer(risk_types, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = RiskTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RiskTypeDetail(APIView):
    """ Retrieve, update or delete a risk type instance """

    def get_object(self, pk):
        try:
            return RiskType.objects.get(pk=pk)
        except RiskType.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        risk_type = self.get_object(pk)
        serializer = RiskTypeSerializer(risk_type)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        risk_type = self.get_object(pk)
        serializer = RiskTypeSerializer(risk_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        risk_type = self.get_object(pk)
        risk_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
