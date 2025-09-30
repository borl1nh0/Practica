from django.shortcuts import render   
from .models import Animal, Protectora , Colaborador
from django.url import path  
from .import views

#Pagina de inicio
def lista_animales(request):
    animales= Animal.objects.all()
    return render(request, 'animales/lista_animales.html'), {'lista_animales':animales }

def lista_protectoras(request):
    protectoras= Protectora.objects.all()
    return render(request, 'animales/lista_protectoras.html'), {'lista_protectoras':protectoras }   

def lista_colaboradores(request):
    colaboradores= Colaborador.objects.all()
    return render(request, 'animales/lista_colaboradores.html'), {'lista_colaboradores':colaboradores }
urlpatterns = [
    path('animales/', views.lista_animales, name='lista_animales'),
    path('protectoras/', views.lista_protectoras, name='lista_protectoras'),
    path('colaboradores/', views.lista_colaboradores, name='lista_colaboradores'),
]