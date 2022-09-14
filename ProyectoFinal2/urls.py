"""ProyectoFinal2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ProyectoGSW import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registrar/', views.registrar),
    path('login/', views.login),
    path('reportes/',views.reportes),
    path('Inicio/',views.inicio),
    path('ADepen/',views.guardardeptes),
    path('APro/',views.formproyecto),
    path('reportes/',views.reportes),
    path('ConsultaDeptes/',views.consultadeptes),
    path('ConsultaPro/',views.consultapro),
    path('Empleados/', views.formempleado),
    path('guardaremp/', views.guardaremp),
    path('AgregarDep/', views.formdep),
    path('guardardep/', views.guardardep),
    path('ConsultaEmp/', views.tabempleado),
    path('ConsultaDepto/', views.tabdepartamento),
    path('guardarpro/', views.guardarpro),
    path('ConsultaSuper/', views.tabsuper),
    path('guardarsuper/', views.guardarsuper),
    path('Supervisor/', views.formsuper),
]