# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

testimage = pygame.image.load('testimage.png').convert_alpha()

#display the shop menu
def display_shop():
    draw_text('position' + str(player_pos),font ,BLACK,10,10)
    if shop_open:
        #shop window
        pygame.draw.rect(screen, GREY, (200, 100, 880, 520))
        #shop border
        pygame.draw.rect(screen, BLACK, (200, 100, 880, 520), 4)
        
        draw_text("Ye olde shoppe" ,magicfont, BLACK, 220,120)
        draw_text("Buy potions and spells to defend yourself against the evil malwares" ,magicfont, BLACK, 220,180)



#define colours
WHITE = (255,255,255)
GREY = (100,100,100)
BLACK = (0,0,0)


#define font
font = pygame.font.SysFont('Futura',30)
magicfont = pygame.font.Font('Heraldic Shadows.otf',30)

# draws text to the screen
def draw_text(text,font,text_col,x,y):
    img = font.render(text, True, text_col)
    screen.blit (img,(x,y))



shop_open = False

#draw shop button
def draw_shopButton():
    # button size
    w, h = 120, 40

    # top-right corner (10px margin)
    x = screen.get_width() - w - 10
    y = 10

    # draw button
    pygame.draw.rect(screen, WHITE, (x, y, w, h))
    
    draw_text("SHOP" ,magicfont, BLACK,(x + w // 2)-35,(y + h // 2-15))

    
    return pygame.Rect(x, y, w, h)   # return button rect for clicking
     






while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    #pygame.draw.circle(screen, "red", player_pos, 40)

    image_rect = testimage.get_rect(center=player_pos)
    screen.blit(testimage, image_rect)
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    if keys[pygame.K_RIGHT]:
        testimage = pygame.transform.flip(testimage,1,0)
        pygame.time.wait(100)

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if shop_rect.collidepoint(event.pos):
            shop_open = not shop_open
        pygame.time.wait(100)

    display_shop()
    shop_rect = draw_shopButton()


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()