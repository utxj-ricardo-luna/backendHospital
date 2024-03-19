from django.contrib import admin
from .models import nacimientos_bebes,seguimiento_pediatria

# Register your models here.
admin.site.register(nacimientos_bebes)
admin.site.register(seguimiento_pediatria)