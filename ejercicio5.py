# Definir la tupla con los meses del año
meses = (
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
)

# Solicitar el número al usuario
numero = int(input("Introduce un número del 1 al 12: "))

# Validar que el número esté dentro del rango correcto
if 1 <= numero <= 12:
    # Restamos 1 porque los índices en las tuplas empiezan en 0
    print(f"El mes correspondiente es: {meses[numero - 1]}")
else:
    print("Número inválido. Debe ser un número entre 1 y 12.")