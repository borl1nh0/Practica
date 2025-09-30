from django.shortcuts import render

# Create your views here.
from .models import Animal, Protectora, Colaborador

def lista_animales(request):
    animales= Animal.objects.all()
    return render(request, 'animales/lista_animales.html', {'lista_animales':animales })

def lista_protectoras(request):
    protectoras= Protectora.objects.all()
    return render(request, 'animales/lista_protectoras.html', {'lista_protectoras':protectoras })  

def lista_colaboradores(request):
    colaboradores= Colaborador.objects.all()
    return render(request, 'animales/lista_colaboradores.html', {'lista_colaboradores':colaboradores }) 
