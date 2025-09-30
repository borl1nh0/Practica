from django.contrib import admin

# Register your models here.

from .models import Animal, Protectora, Colaborador

# Registramos cada modelo para que aparezca en el panel de admin
admin.site.register(Animal)
admin.site.register(Protectora)
admin.site.register(Colaborador)