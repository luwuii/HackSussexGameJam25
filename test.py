import pygame 

BLACK = (0, 0 ,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
screenHeight = 300
screenWidth = 300
#screen

background_colour = (BLACK)
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('GAME Jam')
screen.fill(background_colour)


running = True

while running:
    
    for i in range ((screenHeight) // 50):
        pygame.draw.rect(screen, RED, (1 , 50*i , screenWidth, 1))

    pygame.display.flip()
    
    for event in pygame.event.get():    
        # Check for QUIT event      
        if event.type == pygame.QUIT:
            running = False