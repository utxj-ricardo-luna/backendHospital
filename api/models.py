from django.db import models

# Create your models here.
class nacimientos_bebes(models.Model):
	id_bebe = models.CharField(max_length=50)
	fecha_nacimiento = models.CharField(max_length=50)
	hora_nacimiento = models.CharField(max_length=50)
	lugar_nacimiento = models.CharField(max_length=150)
	peso = models.CharField(max_length=15)
	longitud = models.CharField(max_length=100)
	nombre_padre = models.CharField(max_length=50)
	nombre_madre = models.CharField(max_length=50)
	telefono_contacto = models.CharField(max_length=50)
	email_contacto = models.CharField(max_length=50)
	observaciones = models.CharField(max_length=50)
	tipo_nacimiento = models.CharField(max_length=50)
	frecuencia_cardiaca = models.CharField(max_length=50)
	temperatura = models.CharField(max_length=50)
	presion_arterial_sistolica = models.CharField(max_length=50)
	presion_arterial_diastolica = models.CharField(max_length=50)
	#website = models.URLField(max_length=100)
	#foundation = models.PositiveIntegerField()
    #TextField(blanck=True)
	def __str__(self):
		return self.d_nombre
	
class seguimiento_pediatria(models.Model):
	id_pediatrico = models.CharField(max_length=50)
	id_paciente = models.CharField(max_length=50)
	fecha_seguimiento = models.CharField(max_length=50)
	edad_años = models.CharField(max_length=50)
	peso = models.CharField(max_length=50)
	longitud = models.CharField(max_length=50)
	perimetro_craneal = models.CharField(max_length=50)
	temperatura = models.CharField(max_length=50)
	frecuencia_respiratoria = models.CharField(max_length=50)
	frecuencia_cardiaca = models.CharField(max_length=50)
	presion_arterial_sistolica = models.CharField(max_length=50)
	presion_arterial_diastolica = models.CharField(max_length=50)
	vacunas_administradas = models.CharField(max_length=50)
	examenes_medicos_realizados = models.CharField(max_length=50)
	observaciones = models.CharField(max_length=50)
	#website = models.URLField(max_length=100)
	#foundation = models.PositiveIntegerField()
    #TextField(blanck=True)
	def __str__(self):
		return self.ro_nombre
		

