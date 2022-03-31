from django.contrib import admin
from django.urls import path, include
import APIs

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include("APIs.urls"))
    # path('api-auth/', include('rest_framework.urls'))
]
