from django.contrib import admin
from django.urls import include, path
from risk_types import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('risk_types/', include('risk_types.urls'))
]
