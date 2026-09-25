# Solicitar los dos números al usuario
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Realizar las operaciones
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

# Mostrar los resultados
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")

# Controlar la división entre cero
if num2 != 0:
    division = num1 / num2
    print(f"División: {division}")
else:
    print("División: No es posible dividir entre cero.")