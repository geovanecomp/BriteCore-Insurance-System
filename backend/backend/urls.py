from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('risk-types/', include('risk_types.urls')),
    path('field-types/', include('field_types.urls')),
    path('field/', include('fields.urls'))
]
