# Generated by Django 3.2.4 on 2021-08-04 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoGSW', '0017_remove_empleado_departamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='departamento',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, to='ProyectoGSW.departamento'),
            preserve_default=False,
        ),
    ]
