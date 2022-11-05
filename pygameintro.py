import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner') #sets the game name
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
score_surface = test_font.render('My game',False,('Black'))
score_rect = score_surface.get_rect(center=(400,50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom =(80,300)) #the box moves the whatever's inside it
# snail_x_pos = 600

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

while True:
    #event loop: checks for all types of player input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
           if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
               player_gravity = -20

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                player_gravity = -20

        if event.type == pygame.KEYUP:
            print('key up')

    screen.blit(sky_surface,(0,0)) #places surface on display surface
    screen.blit(ground_surface,(0,300))
    pygame.draw.rect(screen,'red',score_rect,0,20)
    pygame.draw.rect(screen,'green',score_rect,6,20)
    screen.blit(score_surface,score_rect)
    
    screen.blit(snail_surface,snail_rect)
    snail_rect.left -=4
    if snail_rect.right <= 0: snail_rect.left = 800 

    #player
    player_gravity += 1       
    screen.blit(player_surf,player_rect)
    player_rect.y += player_gravity
    if player_rect.bottom >= 300: player_rect.bottom =300

    #collision
    if snail_rect.colliderect(player_rect):
        pygame.quit()
        exit()



    # player_rect.left +=4
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print('jump')


    # if player_rect.colliderect(snail_rect):print('collision')

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())


    
    pygame.display.update();
    clock.tick(60)

    # Moves snail image back and forth on screen
    # screen.blit(snail_surface,(snail_x_pos,270))
    # snail_x_pos -= 4
    # if snail_x_pos < -100:
    #     snail_x_pos = 825
