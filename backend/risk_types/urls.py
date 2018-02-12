from django.urls import path

from . import views

prefix = 'api/v1/risk-types/'

urlpatterns = [
    # path(prefix, views.RiskTypeList.as_view(), name='risk_type'),
    # path(prefix+'<int:pk>', views.RiskTypeDetail.as_view(), name='risk_type_detail'),
]
