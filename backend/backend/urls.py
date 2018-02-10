from django.contrib import admin
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()
# router.register('risk_api', views.GamesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('risk-api', include(router.urls)),

]
