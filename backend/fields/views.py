from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404

from .models import Field
from .serializer import FieldSerializer

class FieldList(APIView):
    """ List all fields, or create a new field """

    def get(self, request, format=None):
        field = Field.objects.all()
        serializer = FieldSerializer(field, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = FieldSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FieldDetail(APIView):
    """ Retrieve, update or delete a field instance """

    def get_object(self, pk):
        try:
            return Field.objects.get(pk=pk)
        except Field.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        field = self.get_object(pk)
        serializer = FieldSerializer(field)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        field = self.get_object(pk)
        serializer = FieldSerializer(field, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        field = self.get_object(pk)
        field.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
