from django.contrib import admin
from django.urls import path, include
from company.views.swagger_ui import swagger_ui


urlpatterns = [
    path('admin/', admin.site.urls),
    path('company/', include('company.urls')),
    path('swagger/', swagger_ui, name='swagger-ui')
]
