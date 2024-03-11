from django.shortcuts import render

# Create your views here.
def registro(request):
    return render(request,"core/registro/registro.html")

def home(request):
    return render(request,"core/home.html")

def iniciosesion(request):
    return render(request,"core/registro/iniciosesion.html")

def registropersonal(request):
    return render(request,"core/ingreso-empleado/registro-personal.html")

def listapersonal(request):
    return render(request,"core/ingreso-empleado/lista-personal.html")

def verpersonal(request):
    return render(request,"core/ver-personal/empleados.html")

def asistencia(request):
    return render(request,"core/asistencia-empleados/asistencia.html")

def contrato(request):
    return render(request,"core/contrato-empleados/contrato.html")

    