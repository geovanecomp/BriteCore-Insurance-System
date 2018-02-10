from django.contrib import admin
from django.urls import include, path
from risks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('risks/', include('risks.urls'))
]
