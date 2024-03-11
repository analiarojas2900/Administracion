from django.urls import path
from . import views

urlpatterns = [
    path('', views.registro, name="registro"),
    path('iniciosesion', views.iniciosesion, name="iniciosesion"),
    path('home', views.home, name="home"),
    path('registropersonal', views.registropersonal, name="registropersonal"),
    path('listapersonal', views.listapersonal, name="listapersonal"),
    path('verpersonal', views.verpersonal, name="verpersonal"),
    path('asistencia', views.asistencia, name="asistencia"),
    path('contrato', views.contrato, name="contrato"),
]

