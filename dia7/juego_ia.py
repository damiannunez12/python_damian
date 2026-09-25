
import pygame
import math
import random

pygame.init()

# ==========================================================
# CONFIGURACIÓN
# ==========================================================

ANCHO = 600
ALTO = 400

ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("LABERINTO FOKIN - INFIERNO 🔥")

reloj = pygame.time.Clock()

# ==========================================================
# COLORES
# ==========================================================

NEGRO = (15, 3, 2)
ROJO_OSCURO = (80, 5, 0)
ROJO = (220, 25, 0)
ROJO_CLARO = (255, 50, 0)
NARANJA = (255, 100, 0)
NARANJA_CLARO = (255, 150, 0)
AMARILLO = (255, 220, 30)
BLANCO = (255, 255, 255)
AZUL = (30, 100, 255)
VERDE = (30, 220, 60)
VERDE_OSCURO = (5, 70, 15)
GRIS = (55, 35, 30)
DORADO = (255, 190, 20)

# ==========================================================
# JUGADOR
# ==========================================================

x = 40
y = 70

velocidad = 4
radio = 10

vidas = 3

# ==========================================================
# META
# ==========================================================

meta = pygame.Rect(540, 340, 30, 30)

# ==========================================================
# PAREDES
# ==========================================================

paredes = [

    pygame.Rect(0, 0, 600, 20),
    pygame.Rect(0, 380, 600, 20),
    pygame.Rect(0, 0, 20, 400),
    pygame.Rect(580, 0, 20, 400),

    pygame.Rect(100, 20, 20, 280),
    pygame.Rect(100, 300, 200, 20),

    pygame.Rect(200, 100, 20, 220),
    pygame.Rect(200, 100, 200, 20),

    pygame.Rect(300, 200, 20, 180),

    pygame.Rect(400, 20, 20, 180),
    pygame.Rect(400, 200, 120, 20),

    pygame.Rect(500, 100, 20, 120),

    pygame.Rect(400, 300, 120, 20)
]

# ==========================================================
# PELOTITAS
# ==========================================================

posiciones_monedas = [

    (55, 120),
    (55, 220),
    (55, 330),

    (150, 60),
    (150, 250),

    (250, 60),
    (250, 150),
    (250, 350),

    (350, 150),
    (350, 250),
    (350, 350),

    (450, 60),
    (450, 150),
    (450, 250),
    (450, 350),

    (550, 60),
    (550, 250),
    (550, 330)
]

monedas = []


def crear_monedas():

    monedas.clear()

    for px, py in posiciones_monedas:

        monedas.append(
            pygame.Rect(
                px - 7,
                py - 7,
                14,
                14
            )
        )


crear_monedas()

# ==========================================================
# FANTASMAS
# ==========================================================

fantasmas = [

    {
        "x": 260,
        "y": 60,
        "velocidad": 1.7,
        "color": (255, 30, 20)
    },

    {
        "x": 150,
        "y": 200,
        "velocidad": 1.5,
        "color": (255, 70, 20)
    },

    {
        "x": 450,
        "y": 150,
        "velocidad": 1.8,
        "color": (255, 20, 40)
    },

    {
        "x": 350,
        "y": 340,
        "velocidad": 1.4,
        "color": (220, 20, 10)
    }
]

# ==========================================================
# FUEGO ANIMADO
# ==========================================================

fuegos = []

for i in range(45):

    fuegos.append({
        "x": random.randint(25, 575),
        "y": random.randint(55, 370),
        "tamano": random.randint(5, 14),
        "velocidad": random.uniform(0.5, 1.5),
        "fase": random.randint(0, 100)
    })

# ==========================================================
# BRASAS VOLANDO
# ==========================================================

brasas = []

for i in range(80):

    brasas.append({
        "x": random.randint(0, ANCHO),
        "y": random.randint(0, ALTO),
        "velocidad": random.uniform(0.5, 2),
        "tamano": random.randint(1, 3)
    })

# ==========================================================
# ESTADO
# ==========================================================

corriendo = True
ganaste = False
perdiste = False

# ==========================================================
# TIEMPO
# ==========================================================

TIEMPO_LIMITE = 120

tiempo_inicial = pygame.time.get_ticks()

# ==========================================================
# FUENTES
# ==========================================================

fuente_grande = pygame.font.Font(None, 40)
fuente_mediana = pygame.font.Font(None, 30)
fuente_pequena = pygame.font.Font(None, 22)

# ==========================================================
# FUNCIONES
# ==========================================================


def jugador_rect(nx, ny):

    return pygame.Rect(
        int(nx - radio),
        int(ny - radio),
        radio * 2,
        radio * 2
    )


# ==========================================================
# COLISIONES
# ==========================================================


def puede_moverse(nx, ny):

    rect = jugador_rect(nx, ny)

    for pared in paredes:

        if rect.colliderect(pared):

            return False

    return True


# ==========================================================
# DIBUJAR LLAMA
# ==========================================================


def dibujar_llama(px, py, tamano):

    # Resplandor

    pygame.draw.circle(
        ventana,
        (100, 15, 0),
        (int(px), int(py)),
        int(tamano * 1.8)
    )

    # Fuego rojo

    pygame.draw.polygon(
        ventana,
        ROJO_CLARO,
        [
            (px, py + tamano),
            (px - tamano, py),
            (px - tamano * 0.5, py + 2),
            (px - tamano * 0.2, py - tamano),
            (px + tamano * 0.4, py - 2),
            (px + tamano * 0.7, py - tamano * 0.6),
            (px + tamano, py + tamano)
        ]
    )

    # Fuego naranja

    pygame.draw.polygon(
        ventana,
        NARANJA,
        [
            (px, py + tamano * 0.7),
            (px - tamano * 0.6, py),
            (px - tamano * 0.2, py + 1),
            (px, py - tamano * 0.6),
            (px + tamano * 0.4, py),
            (px + tamano * 0.6, py + tamano * 0.7)
        ]
    )

    # Fuego amarillo

    pygame.draw.polygon(
        ventana,
        AMARILLO,
        [
            (px, py + tamano * 0.5),
            (px - tamano * 0.3, py),
            (px, py - tamano * 0.35),
            (px + tamano * 0.3, py),
            (px + tamano * 0.4, py + tamano * 0.5)
        ]
    )


# ==========================================================
# DIBUJAR MUCHAS LLAMAS
# ==========================================================


def dibujar_fuegos():

    tiempo = pygame.time.get_ticks() / 100

    for fuego in fuegos:

        variacion = math.sin(
            tiempo * fuego["velocidad"]
            + fuego["fase"]
        )

        tamano = fuego["tamano"] + variacion * 2

        dibujar_llama(
            fuego["x"],
            fuego["y"],
            max(3, tamano)
        )


# ==========================================================
# ACTUALIZAR BRASAS
# ==========================================================


def actualizar_brasas():

    for brasa in brasas:

        brasa["y"] -= brasa["velocidad"]

        brasa["x"] += math.sin(
            brasa["y"] / 20
        ) * 0.5

        if brasa["y"] < 0:

            brasa["y"] = ALTO

            brasa["x"] = random.randint(
                0,
                ANCHO
            )


# ==========================================================
# DIBUJAR BRASAS
# ==========================================================


def dibujar_brasas():

    for brasa in brasas:

        pygame.draw.circle(
            ventana,
            NARANJA_CLARO,
            (
                int(brasa["x"]),
                int(brasa["y"])
            ),
            brasa["tamano"]
        )


# ==========================================================
# DIBUJAR FANTASMA
# ==========================================================


def dibujar_fantasma(fantasma):

    fx = int(fantasma["x"])
    fy = int(fantasma["y"])

    color = fantasma["color"]

    # Aura de fuego

    pygame.draw.circle(
        ventana,
        ROJO_OSCURO,
        (fx, fy),
        22
    )

    # Cabeza

    pygame.draw.circle(
        ventana,
        color,
        (fx, fy),
        15
    )

    # Cuerpo

    pygame.draw.rect(
        ventana,
        color,
        (fx - 15, fy, 30, 13)
    )

    # Cola

    pygame.draw.circle(
        ventana,
        color,
        (fx - 9, fy + 12),
        6
    )

    pygame.draw.circle(
        ventana,
        color,
        (fx + 9, fy + 12),
        6
    )

    # Ojos

    pygame.draw.circle(
        ventana,
        BLANCO,
        (fx - 6, fy - 3),
        5
    )

    pygame.draw.circle(
        ventana,
        BLANCO,
        (fx + 6, fy - 3),
        5
    )

    # Pupilas

    pygame.draw.circle(
        ventana,
        NEGRO,
        (fx - 6, fy - 2),
        2
    )

    pygame.draw.circle(
        ventana,
        NEGRO,
        (fx + 6, fy - 2),
        2
    )


# ==========================================================
# REINICIAR
# ==========================================================


def reiniciar():

    global x
    global y
    global vidas
    global ganaste
    global perdiste
    global tiempo_inicial

    x = 40
    y = 70

    vidas = 3

    ganaste = False
    perdiste = False

    tiempo_inicial = pygame.time.get_ticks()

    crear_monedas()

    posiciones = [
        (260, 60),
        (150, 200),
        (450, 150),
        (350, 340)
    ]

    for i in range(len(fantasmas)):

        fantasmas[i]["x"] = posiciones[i][0]
        fantasmas[i]["y"] = posiciones[i][1]


# ==========================================================
# BUCLE PRINCIPAL
# ==========================================================

while corriendo:

    # ======================================================
    # EVENTOS
    # ======================================================

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:

            corriendo = False

        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_r:

                reiniciar()

            if evento.key == pygame.K_ESCAPE:

                corriendo = False

    # ======================================================
    # MOVIMIENTO
    # ======================================================

    if not ganaste and not perdiste:

        teclas = pygame.key.get_pressed()

        nuevo_x = x
        nuevo_y = y

        if teclas[pygame.K_RIGHT]:
            nuevo_x += velocidad

        if teclas[pygame.K_LEFT]:
            nuevo_x -= velocidad

        if teclas[pygame.K_UP]:
            nuevo_y -= velocidad

        if teclas[pygame.K_DOWN]:
            nuevo_y += velocidad

        # Colisión horizontal

        if puede_moverse(nuevo_x, y):

            x = nuevo_x

        # Colisión vertical

        if puede_moverse(x, nuevo_y):

            y = nuevo_y

    # ======================================================
    # JUGADOR
    # ======================================================

    jugador = jugador_rect(x, y)

    # ======================================================
    # COMER PELOTITAS
    # ======================================================

    for moneda in monedas[:]:

        if jugador.colliderect(moneda):

            monedas.remove(moneda)

    # ======================================================
    # FANTASMAS
    # ======================================================

    if not ganaste and not perdiste:

        for fantasma in fantasmas:

            dx = x - fantasma["x"]
            dy = y - fantasma["y"]

            distancia = math.sqrt(
                dx * dx +
                dy * dy
            )

            if distancia > 0:

                movimiento_x = (
                    dx / distancia
                ) * fantasma["velocidad"]

                movimiento_y = (
                    dy / distancia
                ) * fantasma["velocidad"]

                nuevo_fx = (
                    fantasma["x"] +
                    movimiento_x
                )

                nuevo_fy = (
                    fantasma["y"] +
                    movimiento_y
                )

                fantasma_rect = pygame.Rect(
                    int(nuevo_fx - 14),
                    int(nuevo_fy - 14),
                    28,
                    28
                )

                puede_mover = True

                for pared in paredes:

                    if fantasma_rect.colliderect(pared):

                        puede_mover = False

                        break

                if puede_mover:

                    fantasma["x"] = nuevo_fx
                    fantasma["y"] = nuevo_fy

    # ======================================================
    # COLISIÓN CON FANTASMAS
    # ======================================================

    if not ganaste and not perdiste:

        for fantasma in fantasmas:

            distancia = math.sqrt(
                (x - fantasma["x"]) ** 2 +
                (y - fantasma["y"]) ** 2
            )

            if distancia < 25:

                vidas -= 1

                x = 40
                y = 70

                for f in fantasmas:

                    f["x"] = random.randint(
                        150,
                        500
                    )

                    f["y"] = random.randint(
                        60,
                        350
                    )

                if vidas <= 0:

                    perdiste = True

                break

    # ======================================================
    # VICTORIA
    # ======================================================

    # Hay que comer TODAS las pelotitas

    if len(monedas) == 0:

        if jugador.colliderect(meta):

            ganaste = True

            print(
                "HAS GANADO FOKIN GANADOR, MASIVO!"
            )

    # ======================================================
    # TIEMPO
    # ======================================================

    tiempo_actual = pygame.time.get_ticks()

    segundos = (
        tiempo_actual -
        tiempo_inicial
    ) // 1000

    tiempo_restante = (
        TIEMPO_LIMITE -
        segundos
    )

    if tiempo_restante <= 0:

        tiempo_restante = 0

        perdiste = True

    # ======================================================
    # ACTUALIZAR FUEGO
    # ======================================================

    actualizar_brasas()

    # ======================================================
    # FONDO
    # ======================================================

    ventana.fill(
        (25, 3, 2)
    )

    # ======================================================
    # LAVA
    # ======================================================

    pygame.draw.rect(
        ventana,
        ROJO_OSCURO,
        (0, 350, ANCHO, 50)
    )

    # Ríos de lava

    for i in range(
        0,
        ANCHO,
        35
    ):

        pygame.draw.polygon(
            ventana,
            NARANJA,
            [
                (i, 350),
                (i + 15, 350),
                (i + 25, 400),
                (i + 5, 400)
            ]
        )

        pygame.draw.line(
            ventana,
            AMARILLO,
            (i + 5, 360),
            (i + 15, 395),
            3
        )

    # ======================================================
    # FUEGO DEL MAPA
    # ======================================================

    dibujar_fuegos()

    # ======================================================
    # PAREDES
    # ======================================================

    for pared in paredes:

        # Aura naranja

        pygame.draw.rect(
            ventana,
            ROJO_CLARO,
            pared.inflate(4, 4)
        )

        # Pared

        pygame.draw.rect(
            ventana,
            GRIS,
            pared
        )

        # Líneas de fuego

        pygame.draw.line(
            ventana,
            NARANJA,
            pared.topleft,
            pared.topright,
            2
        )

    # ======================================================
    # BRASAS
    # ======================================================

    dibujar_brasas()

    # ======================================================
    # PELOTITAS
    # ======================================================

    for moneda in monedas:

        # Aura

        pygame.draw.circle(
            ventana,
            ROJO,
            moneda.center,
            10
        )

        # Pelota

        pygame.draw.circle(
            ventana,
            DORADO,
            moneda.center,
            6
        )

        # Brillo

        pygame.draw.circle(
            ventana,
            AMARILLO,
            (
                moneda.centerx - 2,
                moneda.centery - 2
            ),
            2
        )

    # ======================================================
    # META
    # ======================================================

    if len(monedas) == 0:

        pygame.draw.rect(
            ventana,
            VERDE_OSCURO,
            meta
        )

        pygame.draw.rect(
            ventana,
            VERDE,
            meta,
            4
        )

        # Fuego alrededor de la meta

        dibujar_llama(
            530,
            335,
            12
        )

        dibujar_llama(
            570,
            335,
            12
        )

    else:

        # Meta bloqueada

        pygame.draw.rect(
            ventana,
            ROJO_OSCURO,
            meta
        )

        pygame.draw.rect(
            ventana,
            ROJO,
            meta,
            4
        )

        # X

        pygame.draw.line(
            ventana,
            ROJO_CLARO,
            (545, 345),
            (565, 365),
            4
        )

        pygame.draw.line(
            ventana,
            ROJO_CLARO,
            (565, 345),
            (545, 365),
            4
        )

    # ======================================================
    # JUGADOR
    # ======================================================

    # Aura gigante

    pygame.draw.circle(
        ventana,
        ROJO_OSCURO,
        (int(x), int(y)),
        23
    )

    pygame.draw.circle(
        ventana,
        NARANJA,
        (int(x), int(y)),
        17,
        3
    )

    # Jugador

    pygame.draw.circle(
        ventana,
        AZUL,
        (int(x), int(y)),
        radio
    )

    # Ojo

    pygame.draw.circle(
        ventana,
        BLANCO,
        (
            int(x + 3),
            int(y - 3)
        ),
        3
    )

    # ======================================================
    # FANTASMAS
    # ======================================================

    for fantasma in fantasmas:

        dibujar_fantasma(
            fantasma
        )

    # ======================================================
    # HUD
    # ======================================================

    pygame.draw.rect(
        ventana,
        NEGRO,
        (10, 5, 580, 45)
    )

    pygame.draw.rect(
        ventana,
        NARANJA,
        (10, 5, 580, 45),
        2
    )

    # Tiempo

    texto = fuente_pequena.render(
        f"🔥 TIEMPO: {tiempo_restante}",
        True,
        BLANCO
    )

    ventana.blit(
        texto,
        (20, 17)
    )

    # Vidas

    texto = fuente_pequena.render(
        f"❤️ VIDAS: {vidas}",
        True,
        BLANCO
    )

    ventana.blit(
        texto,
        (170, 17)
    )

    # Pelotitas

    comidas = (
        len(posiciones_monedas) -
        len(monedas)
    )

    texto = fuente_pequena.render(
        f"🔥 PELOTITAS: {comidas}/{len(posiciones_monedas)}",
        True,
        DORADO
    )

    ventana.blit(
        texto,
        (290, 17)
    )

    # ======================================================
    # AVISO
    # ======================================================

    if (
        len(monedas) > 0
        and not ganaste
        and not perdiste
    ):

        aviso = fuente_pequena.render(
            "🔥 ¡COME TODAS LAS PELOTITAS! 🔥",
            True,
            AMARILLO
        )

        ventana.blit(
            aviso,
            (170, 55)
        )

    # ======================================================
    # VICTORIA
    # ======================================================

    if ganaste:

        capa = pygame.Surface(
            (ANCHO, ALTO)
        )

        capa.set_alpha(225)

        capa.fill(NEGRO)

        ventana.blit(
            capa,
            (0, 0)
        )

        # Muchísimo fuego

        dibujar_llama(
            80,
            100,
            25
        )

        dibujar_llama(
            520,
            100,
            25
        )

        dibujar_llama(
            100,
            300,
            25
        )

        dibujar_llama(
            500,
            300,
            25
        )

        texto = fuente_grande.render(
            "HAS GANADO",
            True,
            AMARILLO
        )

        rect = texto.get_rect(
            center=(300, 135)
        )

        ventana.blit(
            texto,
            rect
        )

        texto = fuente_grande.render(
            "FOKIN GANADOR",
            True,
            NARANJA
        )

        rect = texto.get_rect(
            center=(300, 180)
        )

        ventana.blit(
            texto,
            rect
        )

        texto = fuente_grande.render(
            "MASIVO!",
            True,
            ROJO_CLARO
        )

        rect = texto.get_rect(
            center=(300, 225)
        )

        ventana.blit(
            texto,
            rect
        )

        texto = fuente_pequena.render(
            "🔥 COMISTE TODAS LAS PELOTITAS 🔥",
            True,
            BLANCO
        )

        rect = texto.get_rect(
            center=(300, 270)
        )

        ventana.blit(
            texto,
            rect
        )

        texto = fuente_pequena.render(
            "Presiona R para jugar otra vez",
            True,
            BLANCO
        )

        rect = texto.get_rect(
            center=(300, 310)
        )

        ventana.blit(
            texto,
            rect
        )

    # ======================================================
    # GAME OVER
    # ======================================================

    if perdiste:

        capa = pygame.Surface(
            (ANCHO, ALTO)
        )

        capa.set_alpha(225)

        capa.fill(NEGRO)

        ventana.blit(
            capa,
            (0, 0)
        )

        dibujar_llama(
            100,
            100,
            25
        )

        dibujar_llama(
            500,
            100,
            25
        )

        texto = fuente_grande.render(
            "GAME OVER",
            True,
            ROJO_CLARO
        )

        rect = texto.get_rect(
            center=(300, 150)
        )

        ventana.blit(
            texto,
            rect
        )

        if vidas <= 0:

            mensaje = "👻 LOS FANTASMAS TE ATRAPARON"

        else:

            mensaje = "🔥 SE TERMINÓ EL TIEMPO"

        texto = fuente_mediana.render(
            mensaje,
            True,
            BLANCO
        )

        rect = texto.get_rect(
            center=(300, 205)
        )

        ventana.blit(
            texto,
            rect
        )

        texto = fuente_pequena.render(
            "Presiona R para volver al infierno",
            True,
            AMARILLO
        )

        rect = texto.get_rect(
            center=(300, 260)
        )

        ventana.blit(
            texto,
            rect
        )

    # ======================================================
    # ACTUALIZAR
    # ======================================================

    pygame.display.flip()

    reloj.tick(60)

pygame.quit()

