from ProyectoGSW.forms import *
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import Template , Context
from ProyectoGSW.models import *
# Create your views here.

class Rep:

    def __init__(self,nombre,departamento):
        self.nombre = nombre
        self.departamento = departamento

class Validar:
    def __init__(self, salario, fecha_nacimiento):
        self.salario = salario
        self.fecha_nacimiento = fecha_nacimiento


#---------------VISTAS-----------------

#Vista Inicio
def inicio(request):    
    return render(request,"inicio.html")

#vista para ingresar al sistema
def login(request):
    if request.GET :
        usuario=request.GET["usuario"]
        password=request.GET["password"]
        objeto = Login.objects.filter(nom_usuario=usuario,password=password) #Select * from login
        if objeto:
            return render(request, "inicio.html")
        else:
            return render(request, "login.html",{"error":"si"})
    else:
        return render(request,"login.html")

#vista para registrar usuario
def registrar(request):
    if request.POST :
        objeto = Login()
        objeto.nom_persona = request.POST["nombrec"]
        objeto.nom_usuario = request.POST["usuario"]
        objeto.password = request.POST["password"]
        objeto.save()
        return render(request, "registrar.html")
    else:
        return render(request, "registrar.html", {"error":"si"})

#Empleado validar a partir de aqui 
def tabempleado(request):
    Cempleado = Empleado.objects.all()
    contexto = {"empleados":Cempleado}
    return render(request, "consulta_emp.html",contexto)

def formempleado(request):
    empleado = FormularioEmpleado()
    return render(request, "empleados.html",{"form":empleado})

def guardaremp(request):
    empleado = FormularioEmpleado(request.POST)
    if empleado.is_valid():
        empleado.save()
        empleado = FormularioEmpleado()
    return render(request, "empleados.html",{"form":empleado})


#Departamento
def tabdepartamento(request):
    Cdepartamentos = Departamento.objects.all()
    contexto = {"departamentos":Cdepartamentos}
    return render(request, "consulta_dep.html",contexto)

def formdep(request):
    departamento = FormularioDepartamento()
    return render(request, "Adepartamentos.html",{"form":departamento})

def guardardep(request):
    departamento = FormularioDepartamento(request.POST)
    if departamento.is_valid():
        departamento.save()
        departamento = FormularioDepartamento()
    return render(request, "Adepartamentos.html",{"form":departamento})

#Dependientes
def consultadeptes(request):
    Cdeptes = Dependiente.objects.all()
    contexto = {"dependientes":Cdeptes}
    return render(request, "consulta_deptes.html", contexto)

def formdeptes(request):
    dependiente = FormularioDependiente()
    return render(request, "Adependientes.html",{"formD":dependiente})

def guardardeptes(request):
    dependiente = FormularioDependiente(request.POST)
    if dependiente.is_valid():
        dependiente.save()
        dependiente = FormularioDependiente()
    return render(request, "Adependientes.html",{"formD":dependiente})

#Proyecto
def consultapro(request):
    Cproyecto = Proyecto.objects.all()
    contexto = {"proyectos":Cproyecto}
    return render(request, "consulta_pro.html", contexto)

def formproyecto(request):
    proyecto = FormularioProyecto()
    return render(request, "Aproyectos.html",{"formP":proyecto})

def guardarpro(request):
    proyecto = FormularioProyecto(request.POST)
    if proyecto.is_valid():
        proyecto.save()
        proyecto = FormularioProyecto()
    return render(request, "Aproyectos.html",{"formP":proyecto})
 
#Supervisor
def tabsuper(request):
    Csuper = Supervisor.objects.all()
    contexto = {"supervisor":Csuper}
    return render(request, "consulta_super.html",contexto)

def formsuper(request):
    supervisor = FormularioSupervisor()
    return render(request, "supervisor.html",{"formS":supervisor})

def guardarsuper(request):
    supervisor = FormularioSupervisor(request.POST)
    if supervisor.is_valid():
        supervisor.save()
        supervisor = FormularioSupervisor()
    return render(request, "supervisor.html",{"formS":supervisor})


#Reportes
def reportes(request):
    Cempleado = Empleado.objects.all()
    contexto = {"empleados":Cempleado}
    return render(request,"reportes.html",{"empleados":Cempleado})



