from django.urls import path
from apps.galeria.views import index, imagem
from apps.galeria.views import buscar, filtro

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
    path('filtro/<str:categoria>', filtro, name='filtro'),
]