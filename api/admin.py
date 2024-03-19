from django.contrib import admin
from .models import c_cliente,c_rol, c_cirugia,c_Solicitud_Cirugias

# Register your models here.
admin.site.register(c_cliente)
admin.site.register(c_rol)
admin.site.register(c_cirugia)
admin.site.register(c_Solicitud_Cirugias)

