# Generated by Django 3.2.4 on 2021-08-01 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoGSW', '0002_alter_empleado_rfc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dependiente',
            name='rfc_empleado',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='empleados_proyecto',
            name='rfc_empleado',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]