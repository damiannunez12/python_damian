# Solicitar tres números al usuario
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))

# Determinar cuál es el mayor usando la función integrada max()
mayor = max(num1, num2, num3)

print(f"El número mayor es: {mayor}")