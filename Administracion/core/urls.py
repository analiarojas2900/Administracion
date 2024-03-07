from django.urls import path
from .views import registro,iniciosesion,home

urlpatterns = [
    path('', registro, name="registro"),
    path('iniciosesion', iniciosesion, name="iniciosesion"),
    path('home', home, name="home"),
] 
