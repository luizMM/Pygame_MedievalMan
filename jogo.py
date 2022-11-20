import pygame

pygame.init()

#==== Tela principal
WIDTH = 600
HEIGHT = 500
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Medieval_MAN')

#==== Assets inicias
PLAYER_WIDTH = 17
PLAYER_HEIGHT = 13

assets = {}
assets['player'] = pygame.image.load('assets/img/cavaleiro 2-1.png').convert_alpha()
assets['player'] = pygame.transform.scale(assets['player'],(PLAYER_WIDTH,PLAYER_HEIGHT))

#==== Loop principal
game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    window.fill((0,0,0))
    pygame.display.update()

pygame.quit()