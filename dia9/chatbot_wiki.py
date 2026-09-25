import random
import wikipedia

# Configurar Wikipedia en español
wikipedia.set_lang("es")


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
            nombre = mensaje_original[
                posicion + len("me llamo "):
            ].strip()

            if nombre:
                self.usuario = nombre.title()

                return f"¡Mucho gusto, {self.usuario}! Es un placer conocerte."

        # Preguntar el nombre
        if "como me llamo" in mensaje:

            if self.usuario:
                return f"Te llamas {self.usuario}."

            return "Todavía no me has dicho tu nombre."

        # Buscar respuesta en la base de conocimiento
        for clave, respuesta in self.base_conocimiento.items():

            if clave in mensaje:

                if self.usuario:
                    return f"{self.usuario}, {respuesta}"

                return respuesta

        # ------------------------------------------------
        # SI NO ENCUENTRA LA RESPUESTA, BUSCAR EN WIKIPEDIA
        # ------------------------------------------------

        try:

            print(f"{self.nombre}: Buscando información en Wikipedia...")

            resultado = wikipedia.summary(
                mensaje_original,
                sentences=2
            )

            if self.usuario:
                return f"{self.usuario}, encontré esto en Wikipedia:\n{resultado}"

            return f"Encontré esto en Wikipedia:\n{resultado}"

        except wikipedia.exceptions.DisambiguationError as e:

            # Wikipedia encontró varios resultados
            opciones = e.options[:5]

            return (
                "Encontré varios resultados relacionados. "
                "Puedes preguntar de forma más específica.\n"
                "Algunas opciones son: "
                + ", ".join(opciones)
            )

        except wikipedia.exceptions.PageError:

            # No existe una página con ese nombre
            pass

        except Exception:

            # Error de conexión u otro problema
            pass

        # ------------------------------------------------
        # RESPUESTA SI NO ENTIENDE
        # ------------------------------------------------

        respuestas_no_entendidas = [
            "No entendí tu mensaje, ¿podrías reformularlo?",
            "¿Podrías decirlo de otra forma?",
            "Todavía estoy aprendiendo, ¿puedes preguntarme algo más claro?",
            "No encontré información sobre eso.",
            "No conozco ese tema todavía."
        ]

        respuesta = random.choice(respuestas_no_entendidas)

        if self.usuario:
            return f"{self.usuario}, {respuesta}"

        return respuesta

    # ------------------------------------------------
    # AGREGAR NUEVO CONOCIMIENTO
    # ------------------------------------------------

    def agregar_conocimiento(self, clave, respuesta):

        self.base_conocimiento[clave.lower()] = respuesta

    # ------------------------------------------------
    # MOSTRAR HISTORIAL
    # ------------------------------------------------

    def mostrar_historial(self):

        print("\n--- HISTORIAL DE CONVERSACIÓN ---")

        if not self.historial:

            print("No hay mensajes guardados.")

        else:

            for i, mensaje in enumerate(
                self.historial,
                start=1
            ):
                print(f"{i}. {mensaje}")

        print("---------------------------------\n")


def main():

    # Crear el chatbot
    bot = Chatbot("Asistente SNPP")

    # ------------------------------------------------
    # AGREGAR CONOCIMIENTOS
    # ------------------------------------------------

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
        "Claro, puedo responder preguntas sencillas, guardar tu nombre, mostrar el historial y buscar información en Wikipedia."
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

    # ------------------------------------------------
    # MENSAJE INICIAL
    # ------------------------------------------------

    print("=" * 55)
    print("          ASISTENTE SNPP")
    print("=" * 55)

    print(f"{bot.nombre}: ¡Hola! 👋")
    print(f"{bot.nombre}: Escribe 'salir' para terminar.")
    print(f"{bot.nombre}: Escribe 'historial' para ver la conversación.")
    print(f"{bot.nombre}: Si no conozco algo, buscaré en Wikipedia.")
    print()

    # ------------------------------------------------
    # BUCLE PRINCIPAL
    # ------------------------------------------------

    while True:

        entrada = input("Tú: ")

        # Evitar mensajes vacíos
        if not entrada.strip():

            print(
                f"{bot.nombre}: "
                "Por favor, escribe algo."
            )

            continue

        # Salir
        if entrada.lower().strip() == "salir":

            print(
                f"{bot.nombre}: "
                "¡Hasta pronto! 👋"
            )

            break

        # Mostrar historial
        if entrada.lower().strip() == "historial":

            bot.mostrar_historial()

            continue

        # Responder
        respuesta = bot.responder(entrada)

        print(f"{bot.nombre}: {respuesta}")
        print()


# ------------------------------------------------
# EJECUTAR PROGRAMA
# ------------------------------------------------

if __name__ == "__main__":
    main()

    