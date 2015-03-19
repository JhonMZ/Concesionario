from django.contrib import admin
from concesionario.apps.ventas.models import Color, Motor, Marca, Categoria, Carro

admin.site.register(Color)
admin.site.register(Motor)
admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Carro)