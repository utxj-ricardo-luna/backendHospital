from django.contrib import admin
from .models import c_cliente,c_rol,c_registrosM

# Register your models here.
admin.site.register(c_cliente)
admin.site.register(c_rol)
admin.site.register(c_registrosM)