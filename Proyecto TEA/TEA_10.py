import pygame
from pygame.locals import *
from recursos import cargar_imagen
import cv2
import random
# Inicializar Pygame
pygame.init()

# Definir constantes
VENTANA_ANCHO = 800
VENTANA_ALTO = 600
FPS = 30

# Configurar ventana principal
ventana = pygame.display.set_mode((VENTANA_ANCHO, VENTANA_ALTO))
pygame.display.set_caption("BIENVENIDO A NUESTRO JUEGO")

# Cargar recursos
fondo_animado = cargar_imagen("C:/Users/ValeriaBravo/Documents/PROYECTOS PYTHON/Proyecto TEA/Imagenes/ninos.gif")

# Definir colores
BLANCO = (255, 255, 255)

def mostrar_menu():
    """Muestra el menú principal."""
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

        # Dibujar elementos
        ventana.fill(BLANCO)
        ventana.blit(fondo_animado, (0, 0))

    
        fuente = pygame.font.Font(None, 36)
        texto = fuente.render("Empieza con esta aventura", True, (0, 0, 0))
        ventana.blit(texto, (50, 50))

    
        boton_empezar = pygame.draw.rect(ventana, (0, 255, 0), (300, 200, 200, 50))
        texto_boton = fuente.render("COMENZAR", True, (0, 0, 0))
        ventana.blit(texto_boton, (330, 210))

        # Verificar clic en el botón
        if pygame.mouse.get_pressed()[0] and boton_empezar.collidepoint(pygame.mouse.get_pos()):
            menu_juegos()

        pygame.display.update()

def menu_juegos():
    """Muestra el menú de juegos."""
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()


        ventana.fill(BLANCO)
        ventana.blit(fondo_animado, (0, 0))

     
        fuente = pygame.font.Font(None, 36)
        boton_juego_1 = pygame.draw.rect(ventana, (255, 0, 0), (100, 200, 200, 50))
        texto_juego_1 = fuente.render("RECONOCER EXPRESIONES", True, (0, 0, 0))
        ventana.blit(texto_juego_1, (150, 210))

        boton_juego_2 = pygame.draw.rect(ventana, (0, 255, 0), (300, 200, 200, 50))
        texto_juego_2 = fuente.render("JUEGO DE PUZZLE", True, (0, 0, 0))
        ventana.blit(texto_juego_2, (310, 210))

        boton_juego_3 = pygame.draw.rect(ventana, (0, 0, 255), (500, 200, 200, 50))
        texto_juego_3 = fuente.render("CONCENTRAZCION Y APRENDISAJE", True, (0, 0, 0))
        ventana.blit(texto_juego_3, (510, 210))

        # Verificar clic en los botones
        if pygame.mouse.get_pressed()[0]:
            if boton_juego_1.collidepoint(pygame.mouse.get_pos()):
                juego_1()
            elif boton_juego_2.collidepoint(pygame.mouse.get_pos()):
                juego_2()

        pygame.display.update()

def juego_1():
    pygame.init()

    # Inicializar la cámara
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 500)  
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 500) 
    cap.set(cv2.CAP_PROP_FPS, 30)  
    if not cap.isOpened():
      print("Error: No se pudo abrir la cámara.")
      exit()

    # Definir categorías y asociar imágenes
    categorias = ["FELIZ", "TRISTE", "ENOJADO", "ASUSTADO"]
    imagenes = [cargar_imagen(f"C:/Users/ValeriaBravo/Documents/PROYECTOS PYTHON/Proyecto TEA/Imagenes/{categoria}.png") for categoria in categorias]

    # Variables para seguimiento del juego
    puntaje = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                cap.release()
                pygame.quit()
                quit()

        # Capturar fotograma de la cámara
        ret, frame = cap.read()

        # Convertir a escala de grises para detección facial
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Inicializar detector de caras
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Mostrar las categorías
        ventana = pygame.display.set_mode((800, 600))
        ventana.fill((255, 255, 255))

        fuente = pygame.font.Font(None, 36)
        for i, categoria in enumerate(categorias):
            texto = fuente.render(categoria, True, (0, 0, 0))
            ventana.blit(texto, (i * 200, 50))

            imagen = pygame.transform.scale(imagenes[i], (150, 150))
            ventana.blit(imagen, (i * 200, 100))


        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)


            for i, categoria in enumerate(categorias):
                if i * 200 < x < (i + 1) * 200 and 50 < y < 250:
                    puntaje += 1

        texto_puntaje = fuente.render(f"Puntaje: {puntaje}", True, (0, 0, 0))
        ventana.blit(texto_puntaje, (10, 10))

    
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = pygame.surfarray.make_surface(frame)
        ventana.blit(frame, (0, 300))

        pygame.display.update()

       
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

  
    cap.release()
    pygame.quit()


def juego_2():
    # Inicializar Pygame
    pygame.init()
    # Definir constantes
    VENTANA_ANCHO = 800
    VENTANA_ALTO = 600
    FPS = 30
    ventana = pygame.display.set_mode((VENTANA_ANCHO, VENTANA_ALTO))
    pygame.display.set_caption("Juego de Puzzle")
    # Definir colores
    BLANCO = (255, 255, 255)

    # Cargar imagen para el puzzle
    imagen_puzzle = cargar_imagen("C:/Users/ValeriaBravo/Documents/PROYECTOS PYTHON/Proyecto TEA/Imagenes/puzzle.png")

    # Dividir la imagen en piezas para el puzzle
    piezas = dividir_imagen(imagen_puzzle)

    # Mezclar las piezas
    random.shuffle(piezas)

    x, y = 50, 50

    puntaje = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

            if event.type == MOUSEBUTTONDOWN:
                # Verificar si se hizo clic en una pieza
                for i, pieza in enumerate(piezas):
                    if pieza[1].collidepoint(pygame.mouse.get_pos()):
                        piezas.pop(i)
                        puntaje += 10

        # Dibujar elementos
        ventana.fill(BLANCO)

        # Dibujar las piezas en la ventana
        for pieza in piezas:
            ventana.blit(pieza[0], pieza[1])

        # Mostrar el puntaje
        fuente = pygame.font.Font(None, 36)
        texto_puntaje = fuente.render(f"Puntaje: {puntaje}", True, (0, 0, 0))
        ventana.blit(texto_puntaje, (10, 10))

        pygame.display.update()

def cargar_imagen(ruta):
    return pygame.image.load(ruta).convert()

def dividir_imagen(imagen):
    piezas = []
    ancho_pieza = imagen.get_width() // 3
    alto_pieza = imagen.get_height() // 3

    for i in range(3):
        for j in range(3):
            x = j * ancho_pieza
            y = i * alto_pieza
            rect = pygame.Rect(x, y, ancho_pieza, alto_pieza)
            superficie = pygame.Surface((ancho_pieza, alto_pieza))
            superficie.blit(imagen, (0, 0), rect)
            piezas.append((superficie, rect))

    return piezas


def main():
    """Función principal."""
    mostrar_menu()

if __name__ == "__main__":
    main()
