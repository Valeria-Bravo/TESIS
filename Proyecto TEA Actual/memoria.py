import pygame
import random
import time

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
WINDOW_TITLE = "Juego de Memoria"
WINDOW_BG_COLOR = (255, 255, 255)

# Configuración de cartas
CARD_WIDTH = 100
CARD_HEIGHT = 150
CARD_COLOR = (0, 0, 0)
CARD_FONT = pygame.font.Font(None, 36)

# Configuración del juego
NUM_CARDS = 8
CARD_IMAGES = ["card1.png", "card2.png", "card3.png", "card4.png"]  # Debes tener imágenes para las cartas

# Función para crear el tablero de cartas
def create_board():
    cards = []
    for _ in range(NUM_CARDS):
        card_image = random.choice(CARD_IMAGES)
        cards.extend([card_image, card_image])
        CARD_IMAGES.remove(card_image)
    random.shuffle(cards)
    return cards

# Función principal del juego
def main():
    # Inicialización de la ventana
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Inicialización de variables del juego
    cards = create_board()
    flipped = [False] * len(cards)
    selected = []
    is_flipping = False

    # Bucle principal del juego
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not is_flipping:
                pos = pygame.mouse.get_pos()
                index = pos[0] // CARD_WIDTH + pos[1] // CARD_HEIGHT * (WINDOW_WIDTH // CARD_WIDTH)
                if not flipped[index]:
                    flipped[index] = True
                    selected.append(index)
                    if len(selected) == 2:
                        is_flipping = True
                        pygame.time.delay(1000)  # Retraso para mostrar las cartas volteadas durante 1 segundo
                        if cards[selected[0]] == cards[selected[1]]:
                            flipped[selected[0]] = True
                            flipped[selected[1]] = True
                        else:
                            flipped[selected[0]] = False
                            flipped[selected[1]] = False
                        selected = []
                        is_flipping = False

        # Dibujar el tablero
        screen.fill(WINDOW_BG_COLOR)
        for i in range(len(cards)):
            if flipped[i]:
                card_image = pygame.image.load(cards[i])
                card_image = pygame.transform.scale(card_image, (CARD_WIDTH, CARD_HEIGHT))
                screen.blit(card_image, (i % (WINDOW_WIDTH // CARD_WIDTH) * CARD_WIDTH, i // (WINDOW_WIDTH // CARD_WIDTH) * CARD_HEIGHT))
            else:
                pygame.draw.rect(screen, CARD_COLOR, (i % (WINDOW_WIDTH // CARD_WIDTH) * CARD_WIDTH, i // (WINDOW_WIDTH // CARD_WIDTH) * CARD_HEIGHT, CARD_WIDTH, CARD_HEIGHT))
        pygame.display.flip()

    pygame.quit()

if __name__ == "_main_":
    main()