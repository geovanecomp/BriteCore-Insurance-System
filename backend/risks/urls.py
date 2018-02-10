from django.urls import path

from . import views

prefix = 'api/v1/risk-types/'

urlpatterns = [
    # path('', views.index, name='index'),
    path(prefix+'<int:pk>', views.get_delete_update_risk_type, name='get_delete_update_risk_type'),
    path(prefix, views.get_post_risk_type, name='get_post_risk_type'),
]
