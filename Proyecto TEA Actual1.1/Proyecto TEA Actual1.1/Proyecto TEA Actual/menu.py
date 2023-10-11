import pygame
import sys
import juego_rostros 
import subprocess
from juego_rostros import jugar
# Inicializa Pygame
pygame.init()

# Configuración de pantalla
screen_width = 800
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Banco de Opciones")


black = (0, 0, 0)
white = (255, 255, 255)
pastel_pink = (255, 209, 220)


font = pygame.font.Font(None, 36)
font_bold = pygame.font.Font(None, 48)


def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color, white)  
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

# Función principal del menú
def main_menu(usuario):
    print(usuario)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if juego_de_rostros_button_rect.collidepoint(event.pos):
                    #subprocess.run(["python", "juego_rostros.py"])
                    #display_message("Felicidades ingresaste al juego")
                    jugar(usuario)
                elif deteccion_de_rostros_button_rect.collidepoint(event.pos):
                    display_message("Felicidades ingresaste al juego")
                elif circuito_de_obstaculos_button_rect.collidepoint(event.pos):
                    display_message("Felicidades ingresaste al juego")
                elif juego_de_emparejamiento_button_rect.collidepoint(event.pos):
                    display_message("Felicidades ingresaste al juego")

       
        background = pygame.image.load("C:/Users/ValeriaBravo/Documents/PROYECTOS PYTHON/Proyecto TEA Actual1.1/Proyecto TEA Actual1.1/Proyecto TEA Actual/Imagenes//fondo_pantalla.jpg")
        background = pygame.transform.scale(background, (screen_width, screen_height))
        screen.fill(white)
        screen.blit(background, (0, 0))

       
        draw_text("Banco de Opciones", font_bold, black, screen, screen_width // 2, 100)
        draw_text("Selecciona tu tipo de terapia", font_bold, black, screen, screen_width // 2, 200)

   
        pygame.draw.ellipse(screen, white, (150, 280, 500, 80))
        pygame.draw.ellipse(screen, white, (150, 380, 500, 80))
        pygame.draw.ellipse(screen, white, (150, 480, 500, 80))
        pygame.draw.ellipse(screen, (240, 240, 240), (150, 580, 500, 80))

        juego_de_rostros_button_rect = pygame.Rect(150, 280, 500, 80)
        deteccion_de_rostros_button_rect = pygame.Rect(150, 380, 500, 80)
        circuito_de_obstaculos_button_rect = pygame.Rect(150, 480, 500, 80)
        juego_de_emparejamiento_button_rect = pygame.Rect(150, 580, 500, 80)

        draw_text("Juego de expresiones", font_bold, black, screen, screen_width // 2, 330)
        draw_text("Detección de rostros", font_bold, black, screen, screen_width // 2, 430)
        draw_text("Reforzamiento de manos", font_bold, black, screen, screen_width // 2, 530)
        draw_text("Juego de memoria", font_bold, black, screen, screen_width // 2, 630)

        pygame.draw.ellipse(screen, pastel_pink, juego_de_rostros_button_rect, 3)
        pygame.draw.ellipse(screen, pastel_pink, deteccion_de_rostros_button_rect, 3)
        pygame.draw.ellipse(screen, pastel_pink, circuito_de_obstaculos_button_rect, 3)
        pygame.draw.ellipse(screen, pastel_pink, juego_de_emparejamiento_button_rect, 3)

        pygame.display.update()


def display_message(message):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(black)
        draw_text(message, font_bold, white, screen, screen_width // 2, screen_height // 2)
        pygame.display.update()

if __name__ == "__main__":
    main_menu()
