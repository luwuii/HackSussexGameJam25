import pygame 
import random
pygame.init()

BLACK = (0, 0 ,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

screenWidth = 1000
screenHeight = 800

#screen
def draw_text(text,font,text_col,x,y):
    img = font.render(text, True, text_col)
    screen.blit (img,(x,y))

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('GAME Jam')
screen.fill(BLACK)


pygame.font.init()
font = pygame.font.SysFont('arial',30)

clock = pygame.time.Clock()

def randomInt(x, y):
   return random.randint(x, y)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, colour, height, width, draw, health):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.draw = draw
        self.health = health
        pygame.draw.rect(self.image,colour,pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()

enemy = []

all_sprites_list = pygame.sprite.Group()

for i in range ((screenHeight) // 100):

    enemy.append(Sprite(RED, 50, 50, False, randomInt(1,5)))
    enemy[i].rect.x = (1)
    enemy[i].rect.y = i * 100
    all_sprites_list.add(enemy[i])

running = True
coins = 0
while running:
    clock.tick(60)
    screen.fill(BLACK)          

    draw_text(("coins " + str(coins)), font ,YELLOW ,250 , 10)   
 
    screen.blit(enemy[1].image, enemy[1].rect)
    for i in range ((screenHeight) // 100):
        rng = randomInt(1,50)
        if rng == 5:
            enemy[i].draw = True

        if enemy[i].draw == True:
            screen.blit(enemy[i].image, enemy[i].rect)
            enemy[i].rect.x += 1
        if enemy[i].rect.x > 100 + screenWidth:
            enemy[i].rect.x = - 100

    pygame.display.flip()

    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for e in enemy:
                if e.rect.collidepoint(pos):
                    e.health = e.health - 1
                    print(e.health)
                    coins += 1
                    if e.health == 0:
                        e.rect.x = -100
                        e.health = randomInt(1,5)
