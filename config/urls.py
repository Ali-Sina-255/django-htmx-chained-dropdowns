
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path('dynamic_forms/', include('dynamic_forms.urls', namespace='dynamic_forms')),
]
