from django.db import models

# Create your models here.

class Departamento (models.Model):
	nombre = models.CharField(max_length=30, unique= True)
	numero = models.IntegerField()
	empleado_encargado = models.CharField(max_length=30)
	fecha_inicio = models.DateField()
	def __str__(self):
		return 'Departamento: %s ,Numero: %s'%(self.nombre,self.numero)

class Supervisor (models.Model):
	nombre = models.CharField(max_length=30, unique= True)
	rfc = models.CharField(max_length=13, unique= True)
	sexos = [
		('F', 'Femenino'),
		('M', 'Masculino')
	]
	sexo = models.CharField(max_length=1, choices=sexos)
	fecha_nacimiento = models.DateField()
	direccion = models.CharField(max_length=30)
	salario = models.IntegerField()
	def __str__(self):
		return 'Nombre: %s, RFC: %s'%(self.nombre,self.rfc)

class Empleado (models.Model):
	rfc = models.IntegerField(unique= True)
	nombre_emp = models.CharField(max_length=50)
	sexos = [
		('F', 'Femenino'),
		('M', 'Masculino')
	]
	sexo = models.CharField(max_length=1, choices=sexos)
	direccion = models.CharField(max_length=30)
	fecha_nacimiento = models.DateField()
	salario = models.IntegerField()
	supervisor = models.ForeignKey(Supervisor, null=False,blank=False,on_delete=models.CASCADE)
	departamento = models.ForeignKey(Departamento,null=False,blank=False,on_delete=models.CASCADE)
	def __str__(self):
		return 'Nombre: %s ,RFC: %s'%(self.nombre_emp,self.rfc)

class Proyecto (models.Model):
	nombre_proyecto = models.CharField(max_length=50, unique= True)
	numero = models.IntegerField()
	nom_local = models.CharField(max_length=30, unique= True)
	departamento = models.ForeignKey(Departamento,null=False,blank=False,on_delete=models.CASCADE)
	def __str__(self):
		return 'Departamento: %s, Nombre Proyecto: %s, Local: %s'%(self.nombre,self.nombre_proyecto,self.nom_local)
	

class Dependiente (models.Model):
	nombre = models.CharField(max_length=30, unique= True)
	sexos = [
		('F', 'Femenino'),
		('M', 'Masculino')
	]
	sexo = models.CharField(max_length=1, choices=sexos)
	fecha_nacimiento = models.DateField()
	empleado_encargado = models.ForeignKey(Empleado, null=False, blank=False, on_delete=models.CASCADE)
	def __str__(self):
		return 'Nombre: %s'%(self.nombre)

class Login (models.Model):
	nom_persona=models.CharField(max_length=24, unique= True)
	nom_usuario=models.CharField(max_length=24, unique= True)
	password=models.CharField(max_length=16)
	def __str__(self):
		return 'Nombre: %s ,Usuario: %s'%(self.nom_persona,self.nom_usuario)