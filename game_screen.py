import pygame
from config import *
from assets import *
from classes import *

def game_screen(janela):
    #clock(fps)
    clock = pygame.time.Clock()

    assets = load_assets()

    all_sprites = pygame.sprite.Group()
    all_monsters = pygame.sprite.Group()
    all_bricks = pygame.sprite.Group()
    all_colisions = pygame.sprite.Group()
    all_moedas = pygame.sprite.Group()
    all_elixir = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_monsters'] = all_monsters
    groups['all_bricks'] = all_bricks
    groups['all_colisions'] = all_colisions
    groups['all_moedas'] = all_moedas
    groups['all_elixir'] = all_elixir

    #all_colisions.add(Parede)

    player = Player(groups,assets)
    all_sprites.add(player)
    all_colisions.add(player)
    zombi = Zombi(groups,assets)
    all_monsters.add(zombi)
    all_sprites.add(zombi)
    vampiro = Vampiro(groups,assets)
    all_monsters.add(vampiro)
    all_sprites.add(vampiro)
    esqueleto = Esqueleto(groups,assets)
    all_sprites.add(esqueleto)
    all_monsters.add(esqueleto)
    demonio = Demonio(groups,assets)
    all_sprites.add(demonio)
    all_monsters.add(demonio)

    #renderiza sprites seguindo a matrix do mapa
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            #renderiza as paredes
            if mapa[i][j] == 0:
                x = 95 + (j) * 30
                y = 65 + (i) * 30
                parede = Parede(x,y,assets[CIMA])
                all_bricks.add(parede)
            elif mapa[i][j] == 1:
                x = 95 + (j) * 30
                y = 65 + (i) * 30
                parede = Parede(x,y,assets[BAIXO])
                all_bricks.add(parede)
            elif mapa[i][j] == 2:
                x = 95 + (j) * 30
                y = 65 + (i) * 30
                parede = Parede(x,y,assets[DEITADO])
                all_bricks.add(parede)
            elif mapa[i][j] == 3:
                x = 95 + (j) * 30
                y = 65 + (i) * 30
                parede = Parede(x,y,assets[ESQUERDO])
                all_bricks.add(parede)
            elif mapa[i][j] == 4:
                x = 95 + (j) * 30
                y = 65 + (i) * 30
                parede = Parede(x,y,assets[DIREITO])
                all_bricks.add(parede)
            elif mapa[i][j] == 5:
                x = 95 + (j) * 30
                y = 65 + (i) * 30
                parede = Parede(x,y,assets[SUP_DIREITO])
                all_bricks.add(parede)
            elif mapa[i][j] == 6:
                x = 95 + (j) * 30
                y = 65 + (i) * 30
                parede = Parede(x,y,assets[SUP_ESQUERDO])
                all_bricks.add(parede)
            elif mapa[i][j] == 7:
                x = 95 + (j) * 30
                y = 65 + (i) * 30
                parede = Parede(x,y,assets[INF_ESQUERDO])
                all_bricks.add(parede)
            elif mapa[i][j] == 11:
                x = 95 + (j) * 30
                y = 65 + (i) * 30
                parede = Parede(x,y,assets[INF_DIREITO])
                all_bricks.add(parede)
            elif mapa[i][j] == 10:
                x = 95 + (j) * 30
                y = 65 + (i) * 30
                parede = Parede(x,y,assets[RETO])
                all_bricks.add(parede)
            #renderiza as moedas
            elif mapa[i][j] == 8:
                x = (95+6) + (j) * 30
                y = (65+6) + (i) * 30
                moeda = Moeda(x,y,assets)
                all_moedas.add(moeda)
            #renderiza os elixir
            elif mapa[i][j] == 9:
                x = (95+6) + (j) * 30
                y = (65+6) + (i) * 30
                elixir = Elixir(x,y,assets)
                all_elixir.add(elixir)


    key_downs = {}
    vidas = 3
    score = 0

    ACABOU = 0
    JOGANDO = 1
    MORREU = 2
    state = JOGANDO

    #loop principal
    pygame.mixer.music.play(loops=-1)
    while state != ACABOU:
        clock.tick(FPS)
        #Trata eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if state == JOGANDO:
                #verifica se apertou a tecla
                if event.type == pygame.KEYDOWN:
                    key_downs[event.key] = True
                    #verifica quais teclas foram apertadas
                    if event.key == pygame.K_UP:
                        player.speedy -= 5
                    if event.key == pygame.K_DOWN:
                        player.speedy += 5
                    if event.key == pygame.K_LEFT:
                        player.speedx -= 5
                    if event.key == pygame.K_RIGHT:
                        player.speedx += 5
                #verifica se soltou a tecla
                if event.type == pygame.KEYUP:
                    if event.key in key_downs and key_downs[event.key]:
                        if event.key == pygame.K_UP:
                            player.speedy += 5
                        if event.key == pygame.K_DOWN:
                            player.speedy -= 5
                        if event.key == pygame.K_LEFT:
                            player.speedx += 5
                        if event.key == pygame.K_RIGHT:
                            player.speedx -= 5
        #Atualiza posição do personagem
        all_sprites.update()

        #verifica se jogador colidiu com as moedas
        if state == JOGANDO:
            encostar = pygame.sprite.spritecollide(player, all_moedas, True, pygame.sprite.collide_mask)
            if len(encostar) > 0:
                score += 100
                
        #verifica se jogador colidiu com os monstros
            colidiu = False
            encostou = pygame.sprite.spritecollide(player,all_monsters, colidiu, pygame.sprite.collide_mask)
            if len(encostou) > 0 and colidiu == False:
                player.kill()
                vidas -= 1
                state = MORREU
        
            #matar = pygame.sprite.spritecollide(player, all_monsters, True, pygame.sprite.collide_mask)
            encosta = pygame.sprite.spritecollide(player, all_elixir, True, pygame.sprite.collide_mask)
            if len(encosta) > 0:
                colidiu = True
                
        #verifica se o jogador morreu   
        if state == MORREU:
            if vidas == 0:
                state = ACABOU
            else:
                state = JOGANDO
                score = score
                player = Player(groups,assets)
                all_sprites.add(player)

        #Gera saídas
        janela.fill((94, 75, 85))

        #renderiza as vidas
        vida_surface = assets[SCORE_FONT].render(chr(9829)*vidas, True, (255,0,0))
        janela.blit(vida_surface, (20,TELA_HEIGHT-35))

        #desenha as paredes, moedas e elixir
        all_bricks.draw(janela)
        all_moedas.draw(janela)
        all_elixir.draw(janela)

        #desenha todsa as sprites na tela
        all_sprites.draw(janela)

        #cria e desenha o score do jogador na tela
        font = pygame.font.SysFont(None, 40)
        texto = font.render('{:08d}'.format(score), False, (255,255,255))
        texto_rect = texto.get_rect()
        texto_rect.centerx = TELA_WIDTH/2
        texto_rect.bottom = 50
        janela.blit(texto,texto_rect)

        #atualza a tela
        pygame.display.update()
    if state == ACABOU:
        pygame.mixer.music.stop()
        state = OVER
        return state