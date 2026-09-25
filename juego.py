import random
import sys
import pygame

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Esquiva los Obstáculos")

# Colores (RGB)
NEGRO = (0, 0, 0)
AZUL = (50, 150, 255)
ROJO = (255, 50, 50)
BLANCO = (255, 255, 255)

# Reloj y configuración
reloj = pygame.time.Clock()
FPS = 60

# Jugador
jugador = pygame.Rect(ANCHO // 2 - 20, ALTO - 60, 40, 40)
velocidad_jugador = 6

# Obstáculos
obstaculos = []
def crear_obstaculo():
    x = random.randint(0, ANCHO - 40)
    return pygame.Rect(x, -40, 40, 40)

for _ in range(5):
    obstaculos.append(crear_obstaculo())

velocidad_obstaculo = 5
puntuacion = 0
fuente = pygame.font.SysFont("Arial", 24)
game_over = False

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not game_over:
        # Controles
        teclas = pygame.key.get_pressed()
        if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) and jugador.left > 0:
            jugador.x -= velocidad_jugador
        if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and jugador.right < ANCHO:
            jugador.x += velocidad_jugador
        if (teclas[pygame.K_UP] or teclas[pygame.K_w]) and jugador.top > 0:
            jugador.y -= velocidad_jugador
        if (teclas[pygame.K_DOWN] or teclas[pygame.K_s]) and jugador.bottom < ALTO:
            jugador.y += velocidad_jugador

        # Mover obstáculos
        for obs in obstaculos:
            obs.y += velocidad_obstaculo
            if obs.top > ALTO:
                obs.x = random.randint(0, ANCHO - 40)
                obs.y = -40
                puntuacion += 10

            # Colisión
            if jugador.colliderect(obs):
                game_over = True

    # Renderizado / Dibujo
    pantalla.fill(NEGRO)

    if not game_over:
        pygame.draw.rect(pantalla, AZUL, jugador)
        for obs in obstaculos:
            pygame.draw.rect(pantalla, ROJO, obs)

        texto_score = fuente.render(f"Puntuación: {puntuacion}", True, BLANCO)
        pantalla.blit(texto_score, (10, 10))
    else:
        texto_go = fuente.render("¡GAME OVER! Presiona X para salir", True, ROJO)
        pantalla.blit(texto_go, (ANCHO // 2 - 180, ALTO // 2))

    pygame.display.flip()
    reloj.tick(FPS)