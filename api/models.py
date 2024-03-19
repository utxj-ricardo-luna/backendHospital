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
		


class Puesto(models.Model):
    ID = models.AutoField(primary_key=True)
    Departamento_ID = models.ForeignKey('Departamento', on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=100, null=False)
    Descripcion = models.TextField()
    Requisitos = models.TextField()
    Salario_Minimo = models.DecimalField(max_digits=10, decimal_places=2)
    Salario_Maximo = models.DecimalField(max_digits=10, decimal_places=2)
    Estatus = models.CharField(max_length=10, choices=(('activo', 'activo'), ('inactivo', 'inactivo')), default='activo')

    def __str__(self):
        return self.Nombre




class Horario(models.Model):
    ID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100, null=False)
    Descripcion = models.TextField()
    Tipo_Jornada = models.CharField(max_length=20, choices=(('diurna', 'diurna'), ('nocturna', 'nocturna'), ('turnos_rotativos', 'turnos_rotativos')), null=False)
    Dia_Laboral = models.CharField(max_length=50)
    Hora_Inicio = models.TimeField()
    Hora_Fin = models.TimeField()

    def __str__(self):
        return self.Nombre



class Personal(models.Model):
    ID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100, null=False)
    Genero = models.CharField(max_length=10, choices=(('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')), null=False)
    Fecha_Nacimiento = models.DateField(null=False)
    Direccion = models.CharField(max_length=255)
    Telefono = models.CharField(max_length=20)
    Correo_Electronico = models.CharField(max_length=100)
    Puesto_ID = models.ForeignKey('Puesto', on_delete=models.CASCADE)
    Horario_ID = models.ForeignKey('Horario', on_delete=models.CASCADE)
    Fecha_Inicio = models.DateField()
    Estatus = models.CharField(max_length=10, choices=(('activo', 'activo'), ('inactivo', 'inactivo')), default='activo')

    def __str__(self):
        return self.Nombre
