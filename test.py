import pygame 
import random

BLACK = (0, 0 ,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
screenWidth = 1000
screenHeight = 800

#screen

background_colour = (BLACK)
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('GAME Jam')
screen.fill(background_colour)

def randomInt(x, y):
   return random.randint(x, y)


class person:
  def __init__ (self, name, rect, speed):
    self.name = name
    self.rect = rect
    self.speed = speed

enemy = []

for i in range ((screenHeight) // 100):
    enemy.append(person(("enemy" + str(i)), (pygame.Rect(1, i*100, randomInt(50,100), randomInt(50,100))), randomINt(1,5)))


running = True

while running:
    for i in range (len(enemy)):
        pygame.draw.rect(screen, RED, enemy[i].rect)
    pygame.display.flip()
    
    for event in pygame.event.get():    
        # Check for QUIT event      
        if event.type == pygame.QUIT:
            running = False