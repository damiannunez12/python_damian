import random


class Chatbot:
    def __init__(self, nombre):
        self.nombre = nombre

        self.base_conocimiento = {
            "hola": "¡Hola! ¿En qué puedo ayudarte?",
            "adios": "¡Hasta luego, que tengas un buen día!",
            "como estas": "Estoy funcionando correctamente, gracias por preguntar.",
            "quien eres": "Soy un chatbot creado para practicar POO en Python."
        }

        self.historial = []
        self.usuario = None

    def responder(self, mensaje):
        mensaje_original = mensaje.strip()
        mensaje = mensaje_original.lower()

        # Guardar mensaje en el historial
        self.historial.append(mensaje_original)

        # Detectar "me llamo..."
        if "me llamo " in mensaje:
            posicion = mensaje.find("me llamo ")
            nombre = mensaje_original[posicion + len("me llamo "):].strip()

            if nombre:
                self.usuario = nombre.title()
                return f"¡Mucho gusto, {self.usuario}! Es un placer conocerte."

        # Buscar respuesta en la base de conocimiento
        for clave, respuesta in self.base_conocimiento.items():
            if clave in mensaje:

                if self.usuario:
                    return f"{self.usuario}, {respuesta}"

                return respuesta

        # Respuesta si no entiende
        respuestas_no_entendidas = [
            "no entendí tu mensaje, ¿podrías reformularlo?",
            "¿podrías decirlo de otra forma?",
            "todavía estoy aprendiendo, ¿puedes preguntarme algo más claro?"
        ]

        if self.usuario:
            return f"{self.usuario}, {random.choice(respuestas_no_entendidas)}"

        return random.choice(respuestas_no_entendidas)

    def agregar_conocimiento(self, clave, respuesta):
        self.base_conocimiento[clave.lower()] = respuesta

    def mostrar_historial(self):
        print("\n--- HISTORIAL DE CONVERSACIÓN ---")

        if not self.historial:
            print("No hay mensajes guardados.")
        else:
            for i, mensaje in enumerate(self.historial, start=1):
                print(f"{i}. {mensaje}")

        print("---------------------------------\n")


def main():
    # Crear el chatbot
    bot = Chatbot("Asistente SNPP")

    # Agregar 3 nuevos conocimientos
    bot.agregar_conocimiento(
        "gracias",
        "¡De nada! Estoy aquí para ayudarte."
    )

    bot.agregar_conocimiento(
        "python",
        "Python es un lenguaje de programación muy utilizado y fácil de aprender."
    )

    bot.agregar_conocimiento(
        "ayuda",
        "Claro, puedo responder preguntas sencillas y guardar el historial."
    )

    bot.agregar_conocimiento(
        "programacion",
        "La programación consiste en crear instrucciones para que una computadora resuelva problemas."
    )

    bot.agregar_conocimiento(
        "variable",
        "Una variable es un espacio con nombre donde se almacena un dato que puede cambiar."
    )

    bot.agregar_conocimiento(
        "funcion",
        "Una función es un bloque de código reutilizable que realiza una tarea específica."
    )

    bot.agregar_conocimiento(
        "bucle",
        "Un bucle permite repetir un bloque de código mientras se cumpla una condición o durante un número determinado de veces."
    )

    bot.agregar_conocimiento(
        "poo",
        "La programación orientada a objetos organiza el código mediante clases y objetos."
    )

    print(f"{bot.nombre}: ¡Hola!")
    print(f"{bot.nombre}: Escribe 'salir' para terminar.")
    print(f"{bot.nombre}: Escribe 'historial' para ver la conversación.\n")

    while True:
        entrada = input("Tú: ")

        # Salir
        if entrada.lower().strip() == "salir":
            print(f"{bot.nombre}: ¡Hasta pronto!")
            break

        # Mostrar historial
        if entrada.lower().strip() == "historial":
            bot.mostrar_historial()
            continue

        # Responder
        respuesta = bot.responder(entrada)

        print(f"{bot.nombre}: {respuesta}")


if __name__ == "__main__":
    main()
