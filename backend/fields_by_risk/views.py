from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework import status

from .models import FieldByRisk
from .serializer import FieldByRiskSerializer

class FieldByRiskViewSet(viewsets.ModelViewSet):
    """ This viewset automatically provides `list` and `detail` FieldByRisk actions. """

    queryset = FieldByRisk.objects.all()
    serializer_class = FieldByRiskSerializer

    @list_route(url_path='list-fields-by-risk')
    def list_fields_by_risk(self, request):
        risk_id = self.request.query_params.get('risk_id', None)

        if risk_id is not None:
            fields_by_risk = FieldByRisk.objects.filter(risk=risk_id)
            serializer = FieldByRiskSerializer(fields_by_risk, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_204_NO_CONTENT)
