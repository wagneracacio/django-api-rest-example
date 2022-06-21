from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('escola/', include('escola.urls')),
    path('admin/', admin.site.urls),
]
