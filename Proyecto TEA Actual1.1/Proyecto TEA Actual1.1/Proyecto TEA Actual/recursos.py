import pygame

def cargar_imagen(ruta):
    """Carga una imagen y la devuelve."""
    return pygame.image.load(ruta).convert()
