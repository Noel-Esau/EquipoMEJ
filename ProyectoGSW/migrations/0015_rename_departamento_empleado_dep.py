# Generated by Django 3.2.4 on 2021-08-04 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoGSW', '0014_empleado_departamento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='departamento',
            new_name='dep',
        ),
    ]