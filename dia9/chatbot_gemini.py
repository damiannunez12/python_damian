import logging
import warnings
from bs4 import GuessedAtParserWarning
import wikipedia
from google import genai

# Desactivar advertencias de BeautifulSoup provenientes de Wikipedia
warnings.filterwarnings("ignore", category=GuessedAtParserWarning)

# Configurar wikipedia en español
wikipedia.set_lang("es")


class Chatbot:
    def __init__(self, nombre):
        self.nombre = nombre
        self.base_conocimiento = {
            "adios": "¡Hasta luego, que tengas un buen día!",
            "quien eres": "Soy un chatbot creado para practicar POO en Python e integrado con Gemini.",
        }
        self.historial = []
        self.usuario = None

        # Inicializar el cliente de Gemini y la sesión de chat con instrucciones de sistema
        try:
            self.cliente = genai.Client()
            self.chat_gemini = self.cliente.chats.create(
                model="gemini-2.5-flash",
                config=genai.types.GenerateContentConfig(
                    system_instruction="Eres un asistente virtual amable y conciso llamado Asistente SNPP."
                ),
            )
        except Exception:
            self.chat_gemini = None

    def responder(self, mensaje):
        mensaje_original = mensaje.strip()
        mensaje = mensaje.lower()

        # Guardar en el historial local
        self.historial.append(mensaje_original)

        # 1. Detectar "me llamo..."
        if "me llamo " in mensaje:
            posicion = mensaje.find("me llamo ")
            nombre = mensaje_original[posicion + len("me llamo ") :].strip()

            if nombre:
                self.usuario = nombre.title()
                return f"¡Mucho gusto, {self.usuario}! Es un placer conocerte."

        # 2. Preguntar el nombre
        if "como me llamo" in mensaje:
            if self.usuario:
                return f"Te llamas {self.usuario}."
            return "Todavía no me has dicho tu nombre."

        # 3. Buscar respuesta en la base de conocimiento local
        for clave, respuesta in self.base_conocimiento.items():
            if clave == mensaje:
                return respuesta

        # 4. Intentar responder con la API de Gemini (mantiene memoria de la sesión)
        if self.chat_gemini:
            try:
                respuesta_gemini = self.chat_gemini.send_message(mensaje_original)
                return respuesta_gemini.text
            except Exception:
                pass

        # 5. Si falla Gemini, usar Wikipedia como alternativa
        try:
            return wikipedia.summary(mensaje_original, sentences=2)
        except Exception:
            return "Lo siento, no pude procesar tu solicitud en este momento."

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
    bot = Chatbot("Asistente SNPP")

    print("=" * 55)
    print("           ASISTENTE SNPP (Conectado a Gemini)")
    print("=" * 55)

    print(f"{bot.nombre}: ¡Hola! 👋")
    print(f"{bot.nombre}: Escribe 'salir' para terminar.")
    print(f"{bot.nombre}: Escribe 'historial' para ver la conversación.")
    print()

    while True:
        entrada = input("Tú: ")

        if not entrada.strip():
            print(f"{bot.nombre}: Por favor, escribe algo.")
            continue

        if entrada.lower().strip() == "salir":
            print(f"{bot.nombre}: ¡Hasta pronto! 👋")
            break

        if entrada.lower().strip() == "historial":
            bot.mostrar_historial()
            continue

        respuesta = bot.responder(entrada)
        print(f"{bot.nombre}: {respuesta}")
        print()


if __name__ == "__main__":
    main()
    