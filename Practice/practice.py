import pygame 
from sys import exit 

pygame.init()
screen = pygame.display.set_mode((800,400)) # establishes window of size width, length in pixels 
pygame.display.set_caption('Practice Game') # sets title of window 
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts/courier_new.ttf', 50) #args: font_type, size


ground = pygame.image.load('graphics/ground.jpg').convert()
text_surface = test_font.render('My game', False, 'Black').convert()
#test_surface.fill('Red')

snail_surface = pygame.image.load('graphics/snail.png').convert_alpha()
snail_surface = pygame.transform.scale(snail_surface, (50,50)).convert_alpha()
snail_rectangle = snail_surface.get_rect(topleft = (800,200))
snail_position = 800

player_surface = pygame.image.load('graphics/player/player.png').convert_alpha()
player_surface = pygame.transform.scale(player_surface, (100,100)).convert_alpha()
player_rectangle = player_surface.get_rect(topleft = (50, 175))

while True:
    # draw all elements
    # update everything
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # checks for user clicking X button to close window 
            pygame.quit()
            exit() # securely breaks out of while loop
        if event.type == pygame.MOUSEMOTION:
            if player_rectangle.collidepoint(event.pos):
                print('collide')
    screen.blit(ground, (0,0)) #block image transfer, put one surface on another args:surface, location
    screen.blit(text_surface,(300, 50))

    snail_rectangle.left -= 4
    if snail_rectangle.right < 0: snail_rectangle.left = 800
    screen.blit(snail_surface, snail_rectangle)
    screen.blit(player_surface, player_rectangle)

    # if player_rectangle.colliderect(snail_rectangle):
    #     print('collide')

    
    pygame.display.update()
    clock.tick(60) #sets framerate ceiling at 60 fps

    # 1:15 in video
