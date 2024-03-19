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
		

class CalendarioCirugia(models.Model):
	c_cliente = models.ForeignKey(c_cliente, on_delete=models.CASCADE)
nombreMedico = models.TextField(max_length=100)
    #cirujano = models.ForeignKey(Cirujano, on_delete=models.CASCADE)
    #sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
fecha = models.DateField()
hora_inicio = models.TimeField()
hora_fin = models.TimeField()
descripcion = models.TextField(max_length=150)
salaOperaciones = models.TextField(max_length=150)
tipoCirugia = models.TextField(max_length=150)