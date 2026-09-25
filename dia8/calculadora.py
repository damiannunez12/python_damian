class Calculadora:
     # No es estrictamente necesario declarar las variables de clase aquí 
     # si se van a usar como atributos de instancia, pero si las dejas, cámbialas a 1 y 2.
     numero1 = None
     numero2 = None

     def __init__(self):
          self.numero1 = 0
          self.numero2 = 0  # <- Corregido: antes decía self.numero = 0

     def sumar(self):
          return self.numero1 + self.numero2 

     def restar(self):
          return self.numero1 - self.numero2

     def multiplicar(self):
          return self.numero1 * self.numero2 
     
     def dividir(self):
          if self.numero2 != 0:
              return self.numero1 / self.numero2 
          else:
              return "El divisor no puede ser cero" 

class CalculadoraCientifica(Calculadora):
    """Calculadora cientifica hereda de Calculadora""" # <- Corregido: Indentación alineada
    historial = None

    def __init__(self):
         super().__init__()  # <- Corregido: Añadido .__init__() para activar la herencia
         self.historial = []

    def factorial(self, n):
         fact = 1
         for x in range(1, n + 1):
              fact = fact * x
         self.historial.append(f"{n}! = {fact}")
         return fact         # <- Tip: Es buena práctica retornar el valor calculado


class CalculadoraProgramador(Calculadora):
     def __init__(self):
          super().__init__()

     def a_binario(self, n):
          return bin(n)     
# --- Prueba del programa ---
casio = Calculadora()
casio.numero1 = 45
casio.numero2 = 30

print(f"Suma: {casio.sumar()}")
print(f"Resta: {casio.restar()}")
print(f"Multiplicación: {casio.multiplicar()}")
print(f"División: {casio.dividir()}")

print("Calculadora cientifica")
casiofx = CalculadoraCientifica()
casiofx.numero1 = 20
casiofx.numero2 = 5

print(f"Suma: {casio.sumar()}")
print(f"Resta: {casio.restar()}")
print(f"Multiplicación: {casio.multiplicar()}")
print(f"División: {casio.dividir()}")
print(casiofx.factorial(5))

print("----------------------")
print(casiofx.historial)

print("calculadora programador")
calcufxp = CalculadoraProgramador
n = 10
print(f"Decimal {n}a binario {calcufxp.a_binario(n)} ")