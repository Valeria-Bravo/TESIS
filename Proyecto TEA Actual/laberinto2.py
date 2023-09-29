import pygame
pygame.init()

# Configuración de la pantalla
ANCHO = 800
ALTO = 600
FPS = 60

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Inicialización de la pantalla
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Laberinto')
reloj = pygame.time.Clock()

# Cargar imágenes
fondo = pygame.image.load("C:/Users/ValeriaBravo/Documents/PROYECTOS PYTHON/Proyecto TEA/Imagenes/muro2.jpg").convert()
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
bola_imagen = pygame.image.load("C:/Users/ValeriaBravo/Documents/PROYECTOS PYTHON/Proyecto TEA/Imagenes/persona2.png").convert_alpha()
bola_imagen = pygame.transform.scale(bola_imagen, (60, 60))

# Definición del laberinto
laberinto = [
    "  XXXXXXXXXXXXXX",
    "X              X",
    "X XXX XXXXXXXX X",
    "X X   X        X",
    "X XX XXXXX XXX X",
    "X              X",
    "XXXXXXX XXXX  XX",
    "X              X",
    "XXXXXXXXXXXXXX  "
]

# Tamaño de cada celda del laberinto
ANCHO_CELDA = 80
ALTO_CELDA = 80
CM_A_PX = 80  # Asumiendo que 1 cm = 80 píxeles

# Posición inicial de la bola
bola_x = ANCHO_CELDA // 2
bola_y = ALTO_CELDA // 2

# Bucle principal
gameOver = False
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    # Detección de teclas para mover la bola
    teclas = pygame.key.get_pressed()
    paso = CM_A_PX  # Mover 1 cm en cada paso

    if teclas[pygame.K_UP] and laberinto[(bola_y - ALTO_CELDA) // ALTO_CELDA][bola_x // ANCHO_CELDA] != 'X':
        bola_y = max(bola_y - paso, 0)
    if teclas[pygame.K_DOWN] and laberinto[(bola_y + ALTO_CELDA) // ALTO_CELDA][bola_x // ANCHO_CELDA] != 'X':
        bola_y = min(bola_y + paso, ALTO - 30)
    if teclas[pygame.K_LEFT] and laberinto[bola_y // ALTO_CELDA][(bola_x - ANCHO_CELDA) // ANCHO_CELDA] != 'X':
        bola_x = max(bola_x - paso, 0)
    if teclas[pygame.K_RIGHT] and laberinto[bola_y // ALTO_CELDA][(bola_x + ANCHO_CELDA) // ANCHO_CELDA] != 'X':
        bola_x = min(bola_x + paso, ANCHO - 30)

    # Limpiar la pantalla
    ventana.blit(fondo, (0, 0))

    # Dibujar el laberinto y la bola
    for i, fila in enumerate(laberinto):
        for j, celda in enumerate(fila):
            if celda == 'X':
                pygame.draw.rect(ventana, NEGRO, (j * ANCHO_CELDA, i * ALTO_CELDA, ANCHO_CELDA, ALTO_CELDA))
    ventana.blit(bola_imagen, (bola_x, bola_y))

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de fotogramas
    reloj.tick(FPS)

# Salir del juego
pygame.quit()
