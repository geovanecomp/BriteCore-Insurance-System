from django.urls import path

from . import views

prefix = 'api/v1/fields/'

urlpatterns = [
    # path(prefix, views.FieldList.as_view(), name='field'),
    # path(prefix+'<int:pk>', views.FieldDetail.as_view(), name='field_detail'),
]
