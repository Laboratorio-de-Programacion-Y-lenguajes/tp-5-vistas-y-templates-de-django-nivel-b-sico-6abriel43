from django.urls import path
from.views import InicioView, PublicacionListView, PublicacionDetailView   

app_name = "publicaciones"

urlpatterns = [
    path('', InicioView.as_view(), name='inicio'),
    path('listado/', PublicacionListView.as_view(), name='lista_publicaciones'),
    path('detalle/<int:publicacion_id>/', PublicacionDetailView.as_view(), name='detalle_publicacion'),
]