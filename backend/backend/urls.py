from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from risk_types import views as risk_types_views
from risks import views as risk_views
from field_types import views as field_types_views
from fields import views as fields_views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('risk-types', risk_types_views.RiskTypeViewSet)
router.register('risk', risk_views.RiskViewSet)
router.register('field-types', field_types_views.FieldTypesViewSet)
router.register('field', fields_views.FieldViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
