import pygame, sys
from pygame.locals import *
# визначаємо константу затримки кадрів
# та інші константи
FPS = 5

WIDTH_DISPLAY=500
HEIGHT_DISPLAY=500

WHITE_COLOR = (255, 255, 255)	
ORANGE_COLOR = (255, 150, 100)
BLACK_COLOR = (0,0,0)
GREEN_COLOR = (0, 255, 0)

COORD_X=220
COORD_Y=200
WIDTH_SQUARE=40
HEIGHT_SQUARE=40
STEP=20
 
# ініціалізація та створення об'єктів
pygame.init()
# pygame.display.set_mode((600, 400))

gameDisplay=pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE)

font = pygame.font.SysFont(None, 25)



pygame.display.set_caption("Maxim game")





run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run=False

    keys=pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and COORD_X>STEP-1:
        COORD_X=COORD_X-STEP
    if keys[pygame.K_RIGHT] and COORD_X<WIDTH_DISPLAY-WIDTH_SQUARE:
        COORD_X=COORD_X+STEP
    if keys[pygame.K_UP] and COORD_Y>STEP-1:
        COORD_Y=COORD_Y-STEP
    if keys[pygame.K_DOWN] and COORD_Y<HEIGHT_DISPLAY-HEIGHT_SQUARE:
        COORD_Y=COORD_Y+STEP
    if COORD_X==0 or COORD_X==WIDTH_DISPLAY-WIDTH_SQUARE or COORD_Y==0 or COORD_Y==HEIGHT_DISPLAY-HEIGHT_SQUARE:
        text_surface = font.render(text ='Game over', antialias=True, color= GREEN_COLOR, background=(0,0,0))
        gameDisplay.blit(text_surface, dest=(100,100))
        pygame.display.update()
        
        



    gameDisplay.fill(BLACK_COLOR) 

    pygame.draw.rect(gameDisplay, (255, 0, 226), [COORD_X, 
                                        COORD_Y, 
                                        WIDTH_SQUARE, 
                                        HEIGHT_SQUARE])
    pygame.display.update()
    clock.tick(FPS)
    

