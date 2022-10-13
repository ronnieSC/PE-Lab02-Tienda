from django.contrib import admin

from .models import Articulo, Ingreso_Detalle, Salida_Detalle

# Register your models here.
admin.site.register(Articulo)
admin.site.register(Ingreso_Detalle)
admin.site.register(Salida_Detalle)
