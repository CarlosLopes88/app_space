from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografias

# Create your views here.

def index(request):
    fotografias = Fotografias.objects.order_by('-data_criacao').filter(publicado=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografias, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografias": fotografia})

def buscar(request):
    fotografias = Fotografias.objects.order_by('-data_criacao').filter(publicado=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET["buscar"]
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, 'galeria/buscar.html', {"cards": fotografias})