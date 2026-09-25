# Definir el diccionario con los estudiantes y sus notas
estudiantes_notas = {
    "Ana": 8.5,
    "Carlos": 9.2,
    "Lucía": 7.0,
    "Mateo": 6.8,
    "Sofia": 9.8
}

# Solicitar el nombre al usuario
nombre = input("Introduce el nombre del estudiante: ")

# Buscar el nombre en el diccionario (ignorando mayúsculas y minúsculas)
# Creamos una versión del diccionario con nombres en minúsculas para buscar fácilmente
diccionario_minusculas = {k.lower(): v for k, v in estudiantes_notas.items()}

if nombre.lower() in diccionario_minusculas:
    nota = diccionario_minusculas[nombre.lower()]
    print(f"La nota de {nombre} es: {nota}")
else:
    print(f"El estudiante '{nombre}' no se encuentra en el registro.")