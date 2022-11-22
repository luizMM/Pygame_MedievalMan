import pygame
from jogo import FPS,QUIT,GAME,TELA_HEIGHT,TELA_WIDTH

def inicial_screen(janela):
    clock = pygame.time.Clock()

    background = pygame.image.load('assets/img/tela_inicial_jogo.png').convert()
    background_rect = background.get_rect()

    rodando = True
    while rodando:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                rodando = False

            if event.type == pygame.KEYUP:
                state = GAME
                rodando = False

        #mostra o tiutlo do jogo e o
        titulo = pygame.image.load('assets/img/Medieval man title-1.png.png').convert_alpha()
        titulo = pygame.transform.scale(titulo,(68*5,68*5))
        titulo_rect = titulo.get_rect()
        titulo_rect.midtop = (TELA_WIDTH/2 - 10, -40)
        janela.blit(background,background_rect)
        janela.blit(titulo,titulo_rect)
        
        #mostra a mensagem de precisonar uma tecla
        fonte = pygame.font.SysFont(None,32)
        prescione = fonte.render('Prescione uma tecla para iniciar', False, (255,255,255))
        prescione_rect = prescione.get_rect()
        prescione_rect.midbottom = (TELA_WIDTH/2, TELA_WIDTH -40)
        janela.blit(prescione,prescione_rect)

        pygame.display.flip()

    return state