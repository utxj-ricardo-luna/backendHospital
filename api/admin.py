from django.contrib import admin
from .models import c_cliente,c_rol, c_dispensacion,c_receta_medica,c_receta_medica_detalles,c_inventario

# Register your models here.
admin.site.register(c_cliente)
admin.site.register(c_rol)


admin.site.register(c_dispensacion)
admin.site.register(c_receta_medica)
admin.site.register(c_receta_medica_detalles)
admin.site.register(c_inventario)