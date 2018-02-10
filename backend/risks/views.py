from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from .models import RiskType
from .serializer import RiskTypeSerializer

@api_view(['GET', 'DELETE', 'PUT'])

def get_delete_update_risk_type(request, pk):
    try:
        risk_type = RiskType.objects.get(pk=pk)
    except RiskType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single risk type
    if request.method == 'GET':
        serializer = RiskTypeSerializer(risk_type)
        return Response(serializer.data)
    # delete a single risk type
    elif request.method == 'DELETE':
        return Response({})
    elif request.method == 'PUT':
        return Response({})

@api_view(['GET', 'POST'])
def get_post_risk_type(request):
    # get all risk types
    if request.method == 'GET':
        risk_types = RiskType.objects.all()
        # To serialize a queryset, should use many=True
        serializer = RiskTypeSerializer(risk_types, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name')
        }
        serializer = RiskTypeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
