from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('publicaciones.urls')), 
    # Incluye las URLs de la app publicaciones
    # TODO: Incluir las rutas de la app publicaciones usando include()
    # Pista: path("", include("publicaciones.urls")),
]