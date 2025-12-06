import pygame 
import random

BLACK = (0, 0 ,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
screenWidth = 1000
screenHeight = 800

#screen

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('GAME Jam')
screen.fill(BLACK)

clock = pygame.time.Clock()

def randomInt(x, y):
   return random.randint(x, y)


class person:
  def __init__ (self, name, rect, speed, draw):
    self.name = name
    self.rect = rect
    self.speed = speed
    self.draw = draw

enemy = []

for i in range ((screenHeight) // 100):
    enemy.append(person(("enemy" + str(i)), (pygame.Rect(1, i*100, randomInt(50,100), randomInt(50,100))), randomInt(1,5), False))

running = True

while running:
    clock.tick(60)
    for i in range (len(enemy)):
        rng = randomInt(1,500)
        if rng == 10:
            enemy[i].draw = True

    
    for i in range (len(enemy)):
        if enemy[i].draw == True:
            pygame.draw.rect(screen, RED, enemy[i].rect)
            enemy[i].rect.x += 1


    pygame.display.flip()

    screen.fill(BLACK)
    for event in pygame.event.get():    
        # Check for QUIT event      
        if event.type == pygame.QUIT:
            running = False