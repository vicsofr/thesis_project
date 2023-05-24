from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Company API",
        default_version='v1',
        description="Company routes for tesk task",
        contact=openapi.Contact(email="onenautm@yandex.ru"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

swagger_info = schema_view.with_ui('swagger', cache_timeout=0)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', swagger_info, name='swagger-ui'),
    path('', RedirectView.as_view(url=reverse_lazy('company-urls'))),
]
