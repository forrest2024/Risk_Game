import pygame 
from sys import exit 

pygame.init()
screen = pygame.display.set_mode((800,400)) # establishes window of size width, length in pixels 
pygame.display.set_caption('Practice Game') # sets title of window 
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts/courier_new.ttf', 50) #args: font_type, size

def display_time():
    time = (pygame.time.get_ticks() - start_time) / 1000
    text_surface = test_font.render(f'Time: {time:.0f}', False, (64,64,64)).convert()
    text_rect = text_surface.get_rect(center = (400,50))
    screen.blit(text_surface, text_rect)
    return time

ground = pygame.image.load('graphics/ground.jpg').convert()

game_title = test_font.render('Practice Game', 0,'Black').convert()
game_title_rect = game_title.get_rect(topleft = (0,0))

start_instr = test_font.render('Press space to start', 0, 'Black').convert()
start_instr_rect = start_instr.get_rect(midbottom = (400,200))

fail_surf = test_font.render('GAME OVER', 0, 'Black', 'Red').convert()
fail_rect = fail_surf.get_rect(midtop = (400,0))

inst_fail = test_font.render('Press space to continue', 0, 'Black').convert()
inst_rect = inst_fail.get_rect(midbottom = (400,400))
# fail_surf = pygame.transform.scale(fail_surf, (800,400))

#test_surface.fill('Red')

snail_surface = pygame.image.load('graphics/snail.png').convert_alpha()
snail_surface = pygame.transform.scale(snail_surface, (50,50)).convert_alpha()
snail_rectangle = snail_surface.get_rect(topleft = (800,200))
snail_position = 800

player_surface = pygame.image.load('graphics/player/player.png').convert_alpha()
player_surface = pygame.transform.scale(player_surface, (100,100)).convert_alpha()
player_rectangle = player_surface.get_rect(topleft = (50, 175))

gravity = -20
game_active = False
start_time = 0
score = 0

timer = pygame.USEREVENT +1
pygame.time.set_timer(timer,900)

while True:
    # draw all elements
    # update everything
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # checks for user clicking X button to close window 
            pygame.quit()
            exit() # securely breaks out of while loop
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.type == pygame.MOUSEBUTTONDOWN and player_rectangle.top > 0:
                    gravity = -20

        if event.type == timer and game_active:
            print('test')
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rectangle.left = 800
                player_rectangle.topleft = (50, 175)
                gravity = -20
                start_time = pygame.time.get_ticks()
    
    # if not game_active:
    #     screen.fill('White')
    #     screen.blit(game_title, game_title_rect)
    #     screen.blit(start_instr, start_instr_rect)
    #     game_active = True

    if game_active:
        
        screen.blit(ground, (0,0)) #block image transfer, put one surface on another args:surface, location
        # pygame.draw.rect(screen,'Pink',text_rect,6)
        # screen.blit(text_surface, text_rect)
        score = display_time()
        

        # snail_rectangle.left -= 4
        # if snail_rectangle.right < 0: snail_rectangle.left = 800
        # screen.blit(snail_surface, snail_rectangle)

        gravity += 1
        player_rectangle.y += gravity
        if player_rectangle.bottom >= 300: player_rectangle.bottom = 300
        screen.blit(player_surface, player_rectangle)

        if snail_rectangle.colliderect(player_rectangle):
            game_active = False
            screen.blit(fail_surf,(0,0))
    else:
        score_message = test_font.render(f'Score: {score:.0f}', 0, 'Black')
        score_rect = score_message.get_rect(midtop = (400,100))
        screen.fill('Red')
        
        screen.blit(player_surface, (350, 200))
        if score == 0:
            screen.blit(start_instr, start_instr_rect)
            screen.blit(game_title, game_title_rect)
        else:
            screen.blit(inst_fail, inst_rect)
            screen.blit(fail_surf, fail_rect)
            screen.blit(score_message, score_rect)
            

        



    


    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print("jump")


    
    pygame.display.update()
    clock.tick(60) #sets framerate ceiling at 60 fps

