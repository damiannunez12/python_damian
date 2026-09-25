from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mostrar/', listar),
    path('saludar/', saludar),                # Ruta general de bienvenida
    path('saludar/<str:nombre>', saludar_nombre), # Ruta con parámetro de nombre
    path('factorial/<int:numero>', factorial),
    path('ver/',inicio_render)
]