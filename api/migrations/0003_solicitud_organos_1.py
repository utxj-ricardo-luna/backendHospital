# Generated by Django 5.0.1 on 2024-03-19 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_c_rol'),
    ]

    operations = [
        migrations.CreateModel(
            name='solicitud_organos_1',
            fields=[
                ('solicitud_ID', models.AutoField(primary_key=True, serialize=False)),
                ('paciente_ID', models.IntegerField()),
                ('medico_ID', models.IntegerField()),
                ('organo_ID', models.IntegerField()),
                ('prioridad', models.CharField(choices=[('urgente', 'Urgente'), ('alta', 'Alta'), ('moderada', 'Moderada')], max_length=255)),
                ('fecha_solicitud', models.DateTimeField()),
                ('dias_espera', models.IntegerField()),
                ('estatus', models.CharField(choices=[('Transplante exitoso', 'Transplante Exitoso'), ('Recuperacion', 'Recuperacion'), ('Pendiente', 'Pendiente')], max_length=255)),
            ],
        ),
    ]