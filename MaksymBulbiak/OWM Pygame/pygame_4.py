# підключаємо модуль
import pygame
 
# визначаємо константу затримки кадрів
# та інші константи 
FPS = 60

WHITE = (255, 255, 255)	
ORANGE = (255, 150, 100)
PURPLE = (128,0,128)
BLUE = (0, 0, 255)

DISPLAY_WIDTH = 400 
DISPLAY_HEIGH = 400 
 
# ініціалізація та створення об'єктів
pygame.init()
# pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGH))

pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGH), pygame.RESIZABLE)

pygame.display.set_caption("My first game")

clock = pygame.time.Clock()
 
# якщо необхідно до циклу відобразити об'єкти на екрані
pygame.display.update()
 
#прапорець включили
crashed = False

# головний цикл
while not crashed:
    pygame.time.delay(100)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run=False

    keys=pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and COORD_X>0:
        COORD_X=COORD_X-DELTA_STEP
    if keys[pygame.K_RIGHT] and COORD_X<WIDTH_DISPLAY-WIDTH_RECTANGLE-DELTA_STEP:
        COORD_X=COORD_X+DELTA_STEP
    if keys[pygame.K_UP] and COORD_Y>DELTA_STEP:
        COORD_Y=COORD_Y-DELTA_STEP
    if keys[pygame.K_DOWN] and COORD_Y<HEIGHT_DISPLAY-HEIGHT_RECTANGLE-DELTA_STEP:
        COORD_Y=COORD_Y+DELTA_STEP


    while run:
        pygame.time.delay(100)
    
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
             run=False

        keys=pygame.key.get_pressed()
    
        if keys[pygame.K_LEFT] and COORD_X>0:
        COORD_X=COORD_X-DELTA_STEP
        if keys[pygame.K_RIGHT] and COORD_X<WIDTH_DISPLAY-WIDTH_RECTANGLE-DELTA_STEP:
        COORD_X=COORD_X+DELTA_STEP
        if keys[pygame.K_UP] and COORD_Y>DELTA_STEP:
        COORD_Y=COORD_Y-DELTA_STEP
        if keys[pygame.K_DOWN] and COORD_Y<HEIGHT_DISPLAY-HEIGHT_RECTANGLE-DELTA_STEP:
        COORD_Y=COORD_Y+DELTA_STEP


        pygame.display.fill(BLACK_COLOR) 

        pygame.draw.rect(gameDisplay, (255,0,0), [COORD_X, 
                                            COORD_Y, 
                                            WIDTH_RECTANGLE, 
                                            HEIGHT_RECTANGLE])
        pygame.display.update().fill(BLACK_COLOR) 

        pygame.draw.rect(gameDisplay, (255,0,0), [COORD_X, 
                                            COORD_Y, 
                                            WIDTH_RECTANGLE, 
                                            HEIGHT_RECTANGLE])
        pygame.display.update()
    
        # затримка кадрів
        clock.tick(FPS)
    
        # цикл обробки подій
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("User asked to quit.")
            elif event.type == pygame.KEYDOWN:
                print("User pressed a key.")
            elif event.type == pygame.KEYUP:
                print("User let go of a key.")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("User pressed a mouse button")

        # ######################
        # зміна об'єктів та інше
        # ######################
        
        # обновлення екрану
        pygame.display.update()

#вихід
pygame.quit()