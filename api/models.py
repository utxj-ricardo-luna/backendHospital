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

#Tabla estudio de
class c_estudio(models.Model):
	d_nombre = models.CharField(max_length=50)
	d_descripcion = models.CharField(max_length=250)


class Estudio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)

class Cita(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    paciente_id = models.IntegerField()  # Se asume que esto es un ID de paciente
    medico_id = models.IntegerField()  # Se asume que esto es un ID de médico
    #tipo_estudio = models.ForeignKey(Estudio, on_delete=models.CASCADE, related_name='citas')

class ResultadoEstudio(models.Model):
    estudio = models.ForeignKey(Estudio, on_delete=models.CASCADE)
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE)
    resultado = models.CharField(max_length=500)
    imagen = models.BinaryField()

class Consumible(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

