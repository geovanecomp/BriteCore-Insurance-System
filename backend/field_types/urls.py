from django.urls import path

from . import views

prefix = 'api/v1/field-types/'

urlpatterns = [
    path(prefix, views.RiskTypeList.as_view(), name='field_type'),
    path(prefix+'<int:pk>', views.RiskTypeDetail.as_view(), name='field_type_detail'),
]
