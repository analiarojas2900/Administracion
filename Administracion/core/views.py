from django.shortcuts import render, redirect
from .forms import EmpleadoForm

# Create your views here.
def registro(request):
    return render(request,"core/registro/registro.html")

def home(request):
    return render(request,"core/home.html")

def iniciosesion(request):
    return render(request,"core/registro/iniciosesion.html")

def registropersonal(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('home')  # Redirige a la URL con nombre 'home'
            except Exception as e:
                # Manejo de errores: puedes imprimir el error para ver qué está pasando
                print(e)
                # También puedes agregar un mensaje de error para mostrar al usuario
                error_message = "Ocurrió un error al guardar el empleado. Por favor, inténtalo de nuevo."
                return render(request, 'core/ingreso-empleado/registro-personal.html', {'form': form, 'error_message': error_message})
    else:
        form = EmpleadoForm()
    return render(request, 'core/ingreso-empleado/registro-personal.html', {'form': form})

    
def listapersonal(request):
    return render(request,"core/ingreso-empleado/lista-personal.html")

def verpersonal(request):
    return render(request,"core/ver-personal/empleados.html")

def asistencia(request):
    return render(request,"core/asistencia-empleados/asistencia.html")

def contrato(request):
    return render(request,"core/contrato-empleados/contrato.html")

    