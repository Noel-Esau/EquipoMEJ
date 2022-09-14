from django.contrib.auth.forms import AuthenticationForm
from django import forms
from ProyectoGSW.models import *

class FormularioEmpleado(forms.ModelForm):
	class Meta:
		model = Empleado
		fields = '__all__'
		widgets = {'fecha_nacimiento':forms.DateInput(attrs={'type':'date'})}

		
class FormularioDepartamento(forms.ModelForm):
	class Meta:
		model = Departamento
		fields = '__all__'
		widgets = {'fecha_inicio':forms.DateInput(attrs={'type':'date'})}

class FormularioDependiente(forms.ModelForm):
	class Meta:
		model = Dependiente
		fields = '__all__'
		widgets = {'fecha_nacimiento':forms.DateInput(attrs={'type':'date'})}

class FormularioProyecto(forms.ModelForm):
	class Meta:
		model = Proyecto
		fields = '__all__'

class FormularioSupervisor(forms.ModelForm):
	class Meta:
		model = Supervisor
		fields = '__all__'
		widgets = {'fecha_nacimiento':forms.DateInput(attrs={'type':'date'})}
	

