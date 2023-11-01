import pygame
pygame.init()
 
class Pared(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/ValeriaBravo/Documents/PROYECTOS PYTHON/Proyecto TEA/Imagenes/muro.jpg").convert()
        self.rect = self.image.get_rect()

class Bola(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/ValeriaBravo/Documents/PROYECTOS PYTHON/Proyecto TEA Actual/Imagenes/correr2.png").convert_alpha()
        self.rect = self.image.get_rect()
 

def construir_mapa(mapa):
    listaMuros =[]
    x=0
    y=0
    for fila in mapa:
        for muro in fila:
            if muro =="X":
                listaMuros.append(pygame.Rect(x,y,80,80))
            x+=80
        x=0
        y+=80
    return listaMuros
 
def dibujar_muro(superficie, rectangulo): 
    pygame.draw.rect(superficie, NEGRO, rectangulo)
 
def dibujar_mapa(superficie, listaMuros): 
    for muro in listaMuros:
        dibujar_muro(superficie, muro)
         
         
ANCHO = 1280
ALTO =720
movil = pygame.Rect(600,400, 40,40)
x=0
y=0
vel=0
alt=0
 
NEGRO = (0,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
 
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Muro')
reloj = pygame.time.Clock()
 
listaPared = pygame.sprite.Group()
pared=Pared()
listaPared.add(pared)
 
listaBola = pygame.sprite.Group()
bola=Bola()
listaBola.add(bola)
 
mapa = [
    " XXXXXXXXXXXXXXX",
    "X   O          X",
    "X XXX XXXXXXXX X",
    "X X   X   T    X",
    "X XX XXXXX XXX X",
    "X     T        X",
    "XXXXXXX XXXX  XX",
    "X              X",
    "XXXXXXXXXXXXXXXX"
]
listaMuros = construir_mapa(mapa)
 
gameOver=False
while not gameOver:
     
    reloj.tick(60)
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver=True
 
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                vel=-5
            elif event.key == pygame.K_RIGHT:
                vel=+5
            elif event.key == pygame.K_UP:
                alt=-5
            elif event.key == pygame.K_DOWN:
                alt=+5
        else:
            vel=0
            alt=0
     
    movil.x += vel
    movil.y += alt
     
    bola.rect.x = movil.x
    bola.rect.y = movil.y
    colisiones=0  
    for muro in listaMuros:
     if movil.colliderect(muro):
        movil.x -= vel
        movil.y -= alt
        colisiones += 1
    if movil.x == 80 and movil.y == 80:  # Si la bola llega a (80, 80)
      print("¡Has ganado!")
      gameOver = True
    if colisiones >= 3:
      print("¡Has perdido! Demasiadas colisiones con los muros.")
      gameOver = True

    ventana.fill(NEGRO)
  
    x=0
    y=0
    for fila in mapa:
        for muro in fila:
            if muro=="X":
                pared.rect.x=x
                pared.rect.y=y
                listaPared.add(pared)
                listaPared.draw(ventana)
            x+=80
        x=0
        y+=80
    listaBola.draw(ventana)    
    dibujar_mapa(ventana,listaMuros)
    pygame.display.flip()
pygame.quit()