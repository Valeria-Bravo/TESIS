import pygame
import sys
import time
import os
import random
import subprocess
from db_connection import conectar_bd, obtener_usuario_id, registrar_puntaje  # Agrega registrar_puntaje

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

# Definir skip_rect como una variable global
skip_rect = None

expresiones = {
    "feliz": "C:/Users/ValeriaBravo/Documents/PROYECTOS PYTHON/Proyecto TEA Actual1.1/Proyecto TEA Actual1.1/Proyecto TEA Actual/Imagenes/categorias_feliz",
    "triste": "C:/Users/ValeriaBravo/Documents/PROYECTOS PYTHON/Proyecto TEA Actual1.1/Proyecto TEA Actual1.1/Proyecto TEA Actual/Imagenes/categorias_triste",
    "enojado": "C:/Users/ValeriaBravo/Documents/PROYECTOS PYTHON/Proyecto TEA Actual1.1/Proyecto TEA Actual1.1/Proyecto TEA Actual/Imagenes/categorias_enojado",
    "asustado": "C:/Users/ValeriaBravo/Documents/PROYECTOS PYTHON/Proyecto TEA Actual1.1/Proyecto TEA Actual1.1/Proyecto TEA Actual/Imagenes/categorias_asustado"
}
# Variable global para llevar un registro de los puntos
puntos = 0
usuario = None
juego_terminado = False

def cargar_imagen_carpeta(carpeta):
    archivos = os.listdir(carpeta)
    imagen = pygame.image.load(os.path.join(carpeta, random.choice(archivos)))
    return pygame.transform.scale(imagen, (200, 200))

def mostrar_texto(texto, x, y, color=WHITE):
    font = pygame.font.Font(None, 36)
    superficie = font.render(texto, True, color)
    rect = superficie.get_rect(center=(x, y))
    window.blit(superficie, rect)

def mostrar_mensaje(mensaje, x, y, color=WHITE):
    mostrar_texto(mensaje, x, y, color)
    pygame.display.update()
    time.sleep(3)

def registrar_puntos(usuario):
    usuario_id = obtener_usuario_id(usuario)
    registrar_puntaje(usuario_id, puntos)

def mostrar_nivel(expresion):
    window.fill(background_color)
    
    carpeta_expresion = expresiones[expresion]
    expresion_imagen = cargar_imagen_carpeta(carpeta_expresion)
    expresion_rect = expresion_imagen.get_rect(center=(150, height // 2))  # Centro lado izquierdo
    window.blit(expresion_imagen, expresion_rect)

    mostrar_texto("¿Qué expresión se puede ver en su rostro?", width // 2, 40)
    
    opciones = ["Feliz", "Triste", "Enojado", "Asustado"]
    for i, opcion in enumerate(opciones):
        boton_rect = pygame.draw.rect(window, WHITE, (400, i * 100 + 100, 200, 50))
        mostrar_texto(opcion, boton_rect.centerx, boton_rect.centery, BLACK)  # Letras negras

    # Botón Continuar
    continuar_rect = pygame.draw.rect(window, WHITE, (600, 450, 150, 50))
    mostrar_texto("Continuar", continuar_rect.centerx, continuar_rect.centery, BLACK)

    # Botón Skip
    global skip_rect  # Usar la variable global skip_rect
    skip_rect = pygame.draw.rect(window, WHITE, (200, 450, 150, 50))
    mostrar_texto("Skip", skip_rect.centerx, skip_rect.centery, BLACK)

    # Mostrar el puntaje actual
    mostrar_texto(f"Puntos: {puntos}", width // 2, 550, BLACK)
    
    pygame.display.update()
    return opciones

def chequear_respuesta(respuesta, carpeta_correcta):
    global puntos

    expresion_correcta = None
    for expresion, carpeta in expresiones.items():
        if expresion == carpeta_correcta:
            expresion_correcta = expresion
            break
    
    print(f"Respuesta seleccionada: {respuesta}")
    print(f"Expresión correcta: {expresion_correcta}")
    
    if respuesta.lower() == expresion_correcta:
        mostrar_mensaje("CORRECTO", width // 2, height // 2, BLUE)
        puntos += 1  # Aumentar los puntos si la respuesta es correcta
        mostrar_texto(f"Puntos: {puntos}", width // 2, 550, BLACK)  # Muestra el puntaje actual
        return True
    else:
        mostrar_mensaje("INCORRECTO", width // 2, height // 2, RED)
        mostrar_mensaje("Vamos, tienes un intento más", width // 2, height // 2 + 50, RED)
        return False

def jugar(temp):
    global puntos, usuario, juego_terminado  # Agrega esta línea para acceder a la variable global
    usuario = temp
    print()

    expresiones_niveles = ["feliz", "triste", "enojado", "asustado"]
    nivel_actual = 0
    contador = 0
    puntos = 0  # Restablece los puntos a cero al comenzar un nuevo juego

    while contador < 3:
        contador += 1
        if nivel_actual == 3:
            nivel_actual = 0

        expresion_correcta = expresiones_niveles[nivel_actual]
        opciones = mostrar_nivel(expresion_correcta)

        seleccionado = False
        acertado = False

        while not seleccionado:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    juego_terminado = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i, opcion in enumerate(opciones):
                        boton_rect = pygame.Rect(400, i * 100 + 100, 200, 50)
                        if boton_rect.collidepoint(event.pos):
                            respuesta = opciones[i]
                            seleccionado = True

                    # Verificar si se hizo clic en el botón "Skip"
                    if skip_rect.collidepoint(event.pos):
                        juego_terminado = True

            if seleccionado:
                acertado = chequear_respuesta(respuesta, expresion_correcta)

        if acertado:
            nivel_actual += 1
        else:
            mostrar_mensaje("INCORRECTO", width // 2, height // 2, RED)
            mostrar_mensaje("Vamos, tienes un intento más", width // 2, height // 2 + 50, RED)
            time.sleep(2)

        window.fill(background_color)
        pygame.display.update()

    registrar_puntos(usuario)
    mostrar_mensaje("¡Felicitaciones, lo lograste!", width // 2, height // 2, BLUE)
    juego_terminado = True

if juego_terminado:
    pygame.quit()