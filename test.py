import pygame 
import random
pygame.init()

BLACK = (0, 0 ,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255,255,255)
GREY = (100,100,100)

screenWidth = 1280
screenHeight = 720

#display the shop menu
def display_shop():
    if shop_open:
        #shop window
        pygame.draw.rect(screen, GREY, (200, 100, 880, 520))
        #shop border
        pygame.draw.rect(screen, BLACK, (200, 100, 880, 520), 4)
        
        draw_text("Ye olde shoppe" ,magicfont, BLACK, 220,120)
        draw_text("Buy potions and spells to defend yourself against the evil malwares" ,magicfont, BLACK, 220,180)

shop_open = False

#draw shop button
def draw_shopButton():
    # button size
    w, h = 120, 40

    # top-left corner (10px margin)
    x = 10
    y = 10

    # draw button
    pygame.draw.rect(screen, WHITE, (x, y, w, h))
    
    draw_text("SHOP" ,magicfont, BLACK,(x + w // 2)-35,(y + h // 2-15))

    
    return pygame.Rect(x, y, w, h)   # return button rect for clicking



#screen
def draw_text(text,font,text_col,x,y):
    img = font.render(text, True, text_col)
    screen.blit (img,(x,y))

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('GAME Jam')
screen.fill(BLACK)


#DEFINING FONTS
pygame.font.init()
font = pygame.font.SysFont('arial',30)
magicfont = pygame.font.Font('Heraldic Shadows.otf',30)

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


for i in range ((screenHeight) // 100):
    enemySize = random.randint(30,70)
    enemy.append(Sprite(RED, enemySize, enemySize, False, (enemySize // 10 - 2)))
    enemy[i].rect.x = (-100)
    enemy[i].rect.y = i * 100

running = True
coins = 0
while running:
    clock.tick(60)
    screen.fill(BLACK)



    draw_text(("coins " + str(coins)), font ,YELLOW ,900, 10)   

    for i in range ((screenHeight) // 100):
        rng = randomInt(1,50)
        if rng == 5:
            enemy[i].draw = True

        if enemy[i].draw == True:
            screen.blit(enemy[i].image, enemy[i].rect)
            enemy[i].rect.x += 1
        if enemy[i].rect.x > 100 + screenWidth:
            enemy[i].rect.x = - 100

    display_shop()
    shop_rect = draw_shopButton()
    
    

    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
            running = False


#-----------------------SHOP------------------------
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if shop_rect.collidepoint(event.pos):
                shop_open = not shop_open
            
#---------------------------------------------------


    if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for e in enemy:
                if e.rect.collidepoint(pos):
                    e.health = e.health - 1
                    coins += 1
                    if e.health == 0:
                        e.rect.x = -100
                        e.health = randomInt(1,5)



    pygame.display.flip()
