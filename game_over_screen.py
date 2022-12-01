import pygame
from config import *

def game_over_screen(janela):
    clock = pygame.time.Clock()

    cabou = True
    while cabou:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                cabou = False
            if event.type == pygame.KEYUP:
                state = GAME
                cabou = False

        janela.fill((0,0,0))

        fonte = pygame.font.Font(None, 22)
        prescione = fonte.render('Prescione qualquer tecla para recomeçar!', False, (255,255,255))
        prescione_rect = prescione.get_rect()
        prescione_rect.centerx = TELA_WIDTH//2
        prescione_rect.centery = TELA_HEIGHT//2 + 40
        janela.blit(prescione,prescione_rect)

        font = pygame.font.Font(None, 40)
        texto = font.render('GAME OVER', False, (255,0,0))
        texto_rect = texto.get_rect()
        texto_rect.centerx = TELA_WIDTH//2
        texto_rect.centery = TELA_HEIGHT//2
        janela.blit(texto,texto_rect)

        pygame.display.flip()
    return state