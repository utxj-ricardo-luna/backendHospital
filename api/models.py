from django.db import models

class c_cliente(models.Model):
    d_nombre = models.CharField(max_length=50)
    d_apellidoPaterno = models.CharField(max_length=50)
    d_apellidoMaterno = models.CharField(max_length=50)
    d_direccion = models.CharField(max_length=150)
    d_telefono = models.CharField(max_length=15)
    d_correo = models.CharField(max_length=100)
    d_contrasena = models.CharField(max_length=50)

    def __str__(self):
        return self.d_nombre

class c_rol(models.Model):
    ro_nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.ro_nombre

class c_receta_medica(models.Model):
    r_id = models.AutoField(primary_key=True)
    r_cita_id = models.CharField(max_length=15)
    r_fecha_hora_registro = models.CharField(max_length=15)
    r_estatus = models.CharField(max_length=15)
    
    def __str__(self):
        return str(self.r_id)

class c_receta_medica_detalles(models.Model):
    rc_id = models.AutoField(primary_key=True)
    rc_recetaId = models.CharField(max_length=15)
    rc_medicamento = models.CharField(max_length=15)
    rc_dosis = models.CharField(max_length=15)
    rc_solicitados = models.CharField(max_length=15)
    rc_precio = models.CharField(max_length=15)
    rc_fecha_venta = models.CharField(max_length=15)
    
    def __str__(self):
        return str(self.rc_id)

class c_inventario(models.Model):
    i_id = models.AutoField(primary_key=True)
    i_codigo = models.CharField(max_length=15)
    i_tipo_presentacion = models.CharField(max_length=15)
    i_via_administracion = models.CharField(max_length=15)
    i_cantidad = models.CharField(max_length=15)
    i_precio_costo = models.FloatField(default=0)
    i_precio_venta = models.FloatField(default=0)
    i_numero_lote = models.CharField(max_length=15)
    i_fecha_caducidad = models.CharField(max_length=15)
    
    def __str__(self):
        return str(self.i_id)


class c_dispensacion(models.Model):
    di_id = models.AutoField(primary_key=True)
    di_recetaId = models.CharField(max_length=15)
    di_medicamento = models.CharField(max_length=15)
    di_dosis = models.CharField(max_length=15)
    di_solicitados = models.CharField(max_length=15)
    di_cantidad = models.CharField(max_length=100)  # Cambiado a CharField con longitud más pequeña
    di_precio = models.CharField(max_length=15)
    di_fecha_venta = models.CharField(max_length=15)
    
    def __str__(self):
        return str(self.di_id)

