from django.conf import settings
from django.db import models
from django.utils import timezone

# --- Modelo Animal ---
class Animal(models.Model):
  
    cuidador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

# --- Modelo Protectora ---
class Protectora(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField()
    
    def __str__(self):
        return self.nombre

# --- Modelo Colaborador ---
class Colaborador(models.Model):
    nombre = models.CharField(max_length=150)
    cargo = models.CharField(max_length=150)
    fecha_entrada_protectora = models.DateTimeField()
    
    def __str__(self):
        return f"{self.nombre} ({self.cargo})"