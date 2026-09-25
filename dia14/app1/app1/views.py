from django.http import HttpResponse
from django.shortcuts import render
lista = ["fiorella", "camila", "vanessa", "sofia"]

def listar(request):
    texto_lista = ", ".join(lista)
    return HttpResponse(texto_lista)

# Esta es para cuando entran a /saludar/ sin nombre
def saludar(request):
    return HttpResponse("¡Hola! Por favor ingresa un nombre en la URL (ej: /saludar/Damian)")

# Esta es para cuando entran con el nombre (ej: /saludar/Damian)
def saludar_nombre(request, nombre):
    texto = f"Hola {nombre}"
    return HttpResponse(texto)

def factorial(request, numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado = resultado * i
    return HttpResponse(f"El factorial de {numero} es {resultado}")

def inicio_render(request):
 return render(request, 'app1/inicio.html')