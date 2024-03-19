from django.db import models

# Create your models here.
class c_cliente(models.Model):
	d_nombre = models.CharField(max_length=50)
	d_apellidoPaterno = models.CharField(max_length=50)
	d_apellidoMaterno = models.CharField(max_length=50)
	d_direccion = models.CharField(max_length=150)
	d_telefono = models.CharField(max_length=15)
	d_correo = models.CharField(max_length=100)
	d_contrasena = models.CharField(max_length=50)
	#website = models.URLField(max_length=100)
	#foundation = models.PositiveIntegerField()
    #TextField(blanck=True)
	def __str__(self):
		return self.d_nombre
	
class c_rol(models.Model):
	ro_nombre = models.CharField(max_length=50)
	#website = models.URLField(max_length=100)
	#foundation = models.PositiveIntegerField()
    #TextField(blanck=True)
	def __str__(self):
		return self.ro_nombre
		

class solicitud_organos_1(models.Model):
	solicitud_ID = models.AutoField(primary_key=True)
	paciente_ID = models.IntegerField()
	medico_ID = models.IntegerField()
	organo_ID = models.IntegerField()
 
	class prioridad_2(models.TextChoices):
		urgente = 'urgente' 
		alta = 'alta'
		moderada = 'moderada'
	prioridad = models.CharField( max_length = 255, choices=prioridad_2.choices)
 
	fecha_solicitud = models.DateTimeField()
	dias_espera = models.IntegerField()
 
	class estatus_paciente(models.TextChoices):
		Transplante_exitoso = 'Transplante exitoso'
		Recuperacion = 'Recuperacion'
		Pendiente = 'Pendiente'
	estatus = models.CharField(  max_length = 255, choices=estatus_paciente.choices)
 
	def __str__(self):
		return self.solicitud_ID
