import pygame
import sys
import time
import os
import random
# Inicializar pygame
pygame.init()


width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Juego de Expresiones Faciales")
background_color = (255, 182, 193)  


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


def cargar_imagen_carpeta(carpeta):
    archivos = os.listdir(carpeta)
    imagen = pygame.image.load(os.path.join(carpeta, random.choice(archivos)))
    return pygame.transform.scale(imagen, (200, 200))


expresiones = {
    "feliz": "C:/Users/ValeriaBravo/Documents/PROYECTOS PYTHON/Proyecto TEA/Imagenes/Feliz",
    "triste": "C:/Users/ValeriaBravo/Documents/PROYECTOS PYTHON/Proyecto TEA/Imagenes/Triste",
    "enojado": "C:/Users/ValeriaBravo/Documents/PROYECTOS PYTHON/Proyecto TEA/Imagenes/Enojado",
    "asustado": "C:/Users/ValeriaBravo/Documents/PROYECTOS PYTHON/Proyecto TEA/Imagenes/Asustado"
}

def cargar_imagen_carpeta(carpeta):
    archivos = os.listdir(carpeta)
    imagen = pygame.image.load(os.path.join(carpeta, random.choice(archivos)))
    return pygame.transform.scale(imagen, (200, 200))  # 5 cm x 5 cm


def mostrar_texto(texto, x, y, color=WHITE):
    font = pygame.font.Font(None, 36)
    superficie = font.render(texto, True, color)
    rect = superficie.get_rect(center=(x, y))
    window.blit(superficie, rect)

def mostrar_mensaje(mensaje, x, y, color=WHITE):
    mostrar_texto(mensaje, x, y, color)
    pygame.display.update()
    time.sleep(3)

def mostrar_nivel(expresion):
    window.fill(background_color)
    
    carpeta_expresion = expresiones[expresion]
    expresion_imagen = cargar_imagen_carpeta(carpeta_expresion)
    expresion_rect = expresion_imagen.get_rect(center=(150, height//2))  # Centro lado izquierdo
    window.blit(expresion_imagen, expresion_rect)

    mostrar_texto("¿Qué expresión se puede ver en su rostro?", width//2, 40)
    
    opciones = ["Feliz", "Triste", "Enojado", "Asustado"]
    for i, opcion in enumerate(opciones):
        boton_rect = pygame.draw.rect(window, WHITE, (400, i * 100 + 100, 200, 50))
        mostrar_texto(opcion, boton_rect.centerx, boton_rect.centery, BLACK)  # Letras negras

    # Botón Continuar
    continuar_rect = pygame.draw.rect(window, WHITE, (600, 450, 150, 50))
    mostrar_texto("Continuar", continuar_rect.centerx, continuar_rect.centery, BLACK)

    # Botón Skip
    skip_rect = pygame.draw.rect(window, WHITE, (200, 450, 150, 50))
    mostrar_texto("Skip", skip_rect.centerx, skip_rect.centery, BLACK)
    
    pygame.display.update()
    return opciones


def chequear_respuesta(respuesta, carpeta_correcta):
 
    expresion_correcta = None
    for expresion, carpeta in expresiones.items():
        if carpeta == carpeta_correcta:
            expresion_correcta = expresion
            break
    
    if respuesta == expresion_correcta:
        mostrar_mensaje("CORRECTO", width//2, height//2, BLUE)
        return True
    else:
        mostrar_mensaje("INCORRECTO", width//2, height//2, RED)
        mostrar_mensaje("Vamos, tienes un intento más", width//2, height//2 + 50, RED)
        return False
    
def jugar():
    expresiones_niveles = ["feliz", "triste", "enojado", "asustado"]
    nivel_actual = 0

    while nivel_actual < 10:
        expresion_correcta = expresiones_niveles[nivel_actual]
        opciones = mostrar_nivel(expresion_correcta)

        seleccionado = False
        acertado = False

        while not seleccionado:
            respuesta = None  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i, opcion in enumerate(opciones):
                        boton_rect = pygame.Rect(400, i * 100 + 100, 200, 50)
                        if boton_rect.collidepoint(event.pos):
                            respuesta = opciones[i]
                            seleccionado = True  # Seleccionado es True cuando se hace clic

            if respuesta is not None:  
                acertado = chequear_respuesta(respuesta, expresion_correcta)

        if acertado:
            nivel_actual += 1
        else:
            mostrar_mensaje("INCORRECTO", width//2, height//2, RED)
            mostrar_mensaje("Vamos, tienes un intento más", width//2, height//2 + 50, RED)
            time.sleep(2) 

      
        window.fill(background_color)
        pygame.display.update()

    mostrar_mensaje("¡Felicitaciones, lo lograste!", width//2, height//2, BLUE)
    pygame.quit()
    sys.exit()
jugar()

