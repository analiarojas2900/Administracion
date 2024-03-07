from django.shortcuts import render

# Create your views here.
def registro(request):
    return render(request,"core/registro.html")

def home(request):
    return render(request,"core/home.html")

def iniciosesion(request):
    return render(request,"core/iniciosesion.html")