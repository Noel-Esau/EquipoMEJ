# Generated by Django 3.2.4 on 2021-08-09 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoGSW', '0028_alter_empleado_supervisor'),
    ]

    operations = [
        migrations.AddField(
            model_name='supervisor',
            name='direccion',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supervisor',
            name='salario',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]