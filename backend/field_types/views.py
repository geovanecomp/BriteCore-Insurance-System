from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404

from .models import FieldType
from .serializer import FieldTypeSerializer

class FieldTypeList(APIView):
    """ List all field types, or create a new field type"""

    def get(self, request, format=None):
        field_types = FieldType.objects.all()
        serializer = FieldTypeSerializer(field_types, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = FieldTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FieldTypeDetail(APIView):
    """ Retrieve, update or delete a field type instance """

    def get_object(self, pk):
        try:
            return FieldType.objects.get(pk=pk)
    except FieldType.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        field_type = self.get_object(pk)
        serializer = FieldTypeSerializer(field_type)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        field_type = self.get_object(pk)
        serializer = FieldTypeSerializer(field_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        field_type = self.get_object(pk)
        field_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
