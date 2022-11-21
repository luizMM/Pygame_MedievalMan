import pygame
import random
from os import path

from config import IMG_DIR, FPS, GAME, QUIT


def tela_inicio(screen):

    clock = pygame.time.Clock()
    
    titulo = pygame.image.load(path.join(IMG_DIR,'Medieval man gif.png')).convert()
    titulo_rect = titulo.get_rect()
    background = pygame.image.load(path.join(IMG_DIR, 'tela_inicial_jogo.png')).convert()
    background_rect = background.get_rect()

    running = True
    while running:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                state = GAME
                running = False

        screen.blit(background, background_rect)
        screen.blit(titulo,titulo_rect)

        pygame.display.flip()

    return state
