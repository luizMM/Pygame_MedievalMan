#importa pacotes
#inicialização
import pygame
from mapa import mapa
import random
#from inicial_screen import inicial_screen

pygame.init()

#FPS e tamanhos
FPS = 30
TELA_WIDTH = 600
TELA_HEIGHT = 650
L_MAPA = 224*2
C_MAPA = 288*2

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 45
MONSTER_WIDTH = 55
MONSTER_HEIGHT = 50

INIT = 0
GAME = 1
QUIT = 2

#Telas principal do jogo
janela = pygame.display.set_mode((TELA_WIDTH,TELA_HEIGHT))
pygame.display.set_caption('Medieval_man')

#assets
def load_assets():
    assets = {}
    assets['mapa'] = pygame.image.load('assets/img/Mapa v2-1.png-1.png.png').convert_alpha()
    assets['mapa'] = pygame.transform.scale(assets['mapa'],(L_MAPA,C_MAPA))
    assets['player'] = pygame.image.load('assets/img/cavaleiro 2-1.png.png').convert_alpha()
    assets['player'] = pygame.transform.scale(assets['player'],(PLAYER_WIDTH,PLAYER_HEIGHT))
    assets['vida'] = pygame.image.load('assets/img/Coracao_vida-1.png.png').convert_alpha()
    assets['vida'] = pygame.transform.scale(assets['vida'],(40,40))
    assets['zombi'] = pygame.image.load('assets/img/Zombi jogo-1.png.png').convert_alpha()
    assets['zombi'] = pygame.transform.scale(assets['zombi'],(MONSTER_WIDTH,MONSTER_HEIGHT))
    assets['esqueleto'] = pygame.image.load('assets/img/Esqueleto jogo-1.png.png').convert_alpha()
    assets['esqueleto'] = pygame.transform.scale(assets['esqueleto'], (MONSTER_WIDTH,MONSTER_HEIGHT))
    assets['vampiro'] = pygame.image.load('assets/img/Vampiro jogo-1.png.png').convert_alpha()
    assets['vampiro'] = pygame.transform.scale(assets['vampiro'], (MONSTER_WIDTH,MONSTER_HEIGHT))
    assets['moeda'] = pygame.image.load('assets/img/Moeda-1.png.png').convert_alpha()
    assets['moeda'] = pygame.transform.scale(assets['moeda'], (16,16))
    assets['elixir'] = pygame.image.load('assets/img/Pocao poderosa-1.png.png').convert_alpha()
    assets['elixir'] = pygame.transform.scale(assets['elixir'], (16,16))

    assets['deitado'] = pygame.image.load('assets/img/Parte deitada-1.png.png').convert()
    assets['deitado'] = pygame.transform.scale(assets['deitado'], (30,30))
    assets['cima'] = pygame.image.load('assets/img/Parte cima-1.png.png').convert()
    assets['cima'] = pygame.transform.scale(assets['cima'], (30,30))
    assets['baixo'] = pygame.image.load('assets/img/Parte baixo-1.png.png').convert()
    assets['baixo'] = pygame.transform.scale(assets['baixo'], (30,30))
    assets['reto'] = pygame.image.load('assets/img/Parte reta-1.png.png').convert()
    assets['reto'] = pygame.transform.scale(assets['reto'], (30,30))
    assets['esquerdo'] = pygame.image.load('assets/img/Parte esquerda-1.png.png').convert()
    assets['esquerdo'] = pygame.transform.scale(assets['esquerdo'], (30,30))
    assets['direito'] = pygame.image.load('assets/img/Parte direita-1.png.png').convert()
    assets['direito'] = pygame.transform.scale(assets['direito'], (30,30))
    assets['sup direito'] = pygame.image.load('assets/img/canto sup direito-1.png.png').convert()
    assets['sup direito'] = pygame.transform.scale(assets['sup direito'], (30,30))
    assets['sup esquerdo'] = pygame.image.load('assets/img/canto sup esquerda-1.png.png').convert()
    assets['sup esquerdo'] = pygame.transform.scale(assets['sup esquerdo'], (30,30))
    assets['inf direito'] = pygame.image.load('assets/img/canto inf direito-1.png.png').convert()
    assets['inf direito'] = pygame.transform.scale(assets['inf direito'], (30,30))
    assets['inf esquerdo'] = pygame.image.load('assets/img/canto inf esquerdo-1.png.png').convert()
    assets['inf esquerdo'] = pygame.transform.scale(assets['inf esquerdo'], (30,30))
    return assets

#classe jogador
class Player(pygame.sprite.Sprite):
    def __init__(self,groups,assets):
        pygame.sprite.Sprite.__init__(self)
        #Construção personagem
        self.image = assets['player']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = TELA_WIDTH/2 + 5
        self.rect.bottom = TELA_HEIGHT - 90
        self.speedx = 0
        self.speedy = 0
        self.groups = groups
        self.assets = assets
    def update(self):
        #nova posicao
        bkpx = self.rect.x
        bkpy = self.rect.y
        #atualiza posição da nave
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        i = (self.rect.x + (PLAYER_WIDTH//2) - 95) // 30
        j = (self.rect.y + (PLAYER_HEIGHT//2)- 65) // 30
        #ver se as posicoes e maior que o mapa
        if i >= 0 and i < len(mapa[0]) and j >= 0 and j < len(mapa):
            if mapa[j][i] in [0,1,2,3,4,5,6,7,10,11]:
                self.rect.x = bkpx  
                self.rect.y = bkpy
                print('nao pode mover')
        #mantém dento da tela
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > TELA_HEIGHT:
            self.rect.bottom = TELA_HEIGHT
        if self.rect.right > TELA_WIDTH:
            self.rect.right = TELA_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

class Zombi(pygame.sprite.Sprite):
    def __init__(self,groups,assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['zombi']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = TELA_WIDTH/2 + 15
        self.rect.bottom = TELA_HEIGHT/2
        self.speedx = random.randint(0,10)
        self.speedy = random.randint(0,10)
        self.groups = groups
        self.assets = assets
    def update(self):
        bkpx = self.rect.x
        bkpy = self.rect.y
        self.rect.x += self.speedx
        self.rect.y += self.speedy

class Vampiro(pygame.sprite.Sprite):
    def __init__(self,groups,assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['vampiro']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = TELA_WIDTH/2 - 10
        self.rect.bottom = TELA_HEIGHT/2
        self.speedx = 0
        self.speedy = 0
        self.groups = groups
        self.assets = assets

class Esqueleto(pygame.sprite.Sprite):
    def __init__(self,groups,assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['esqueleto']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = TELA_WIDTH/2 - 10
        self.rect.bottom = TELA_HEIGHT/2 + 30
        self.speedx = 0
        self.speedy = 0
        self.groups = groups
        self.assets = assets

class Parede(pygame.sprite.Sprite):
    def __init__(self,x,y,assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Moeda(pygame.sprite.Sprite):
    def __init__(self,x,y,assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['moeda']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Elixir(pygame.sprite.Sprite):
    def __init__(self,x,y,assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['elixir']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#tela inicial do jogo
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
        janela.blit(background,background_rect)

        titulo = pygame.image.load('assets/img/Medieval man title-1.png.png').convert_alpha()
        titulo = pygame.transform.scale(titulo,(68*5,68*5))
        titulo_rect = titulo.get_rect()
        titulo_rect.midtop = (TELA_WIDTH/2 - 10, -40)
        janela.blit(titulo,titulo_rect)
        
        #mostra a mensagem de precisonar uma tecla
        fonte = pygame.font.SysFont(None,32)
        prescione = fonte.render('Prescione uma tecla para iniciar', False, (255,255,255))
        prescione_rect = prescione.get_rect()
        prescione_rect.midbottom = (TELA_WIDTH/2, TELA_WIDTH -40)
        janela.blit(prescione,prescione_rect)

        pygame.display.flip()

    return state

#tela do jogo
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


    #renderiza sprites seguindo a matrix do mapa
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            #renderiza as paredes
            if mapa[i][j] == 0:
                x = 95 + (j) * 30
                y = 65 + (i) * 30
                parede = Parede(x,y,assets['cima'])
                all_bricks.add(parede)
            elif mapa[i][j] == 1:
                x = 95 + (j) * 30
                y = 65 + (i) * 30
                parede = Parede(x,y,assets['baixo'])
                all_bricks.add(parede)
            elif mapa[i][j] == 2:
                x = 95 + (j) * 30
                y = 65 + (i) * 30
                parede = Parede(x,y,assets['deitado'])
                all_bricks.add(parede)
            elif mapa[i][j] == 3:
                x = 95 + (j) * 30
                y = 65 + (i) * 30
                parede = Parede(x,y,assets['esquerdo'])
                all_bricks.add(parede)
            elif mapa[i][j] == 4:
                x = 95 + (j) * 30
                y = 65 + (i) * 30
                parede = Parede(x,y,assets['direito'])
                all_bricks.add(parede)
            elif mapa[i][j] == 5:
                x = 95 + (j) * 30
                y = 65 + (i) * 30
                parede = Parede(x,y,assets['sup direito'])
                all_bricks.add(parede)
            elif mapa[i][j] == 6:
                x = 95 + (j) * 30
                y = 65 + (i) * 30
                parede = Parede(x,y,assets['sup esquerdo'])
                all_bricks.add(parede)
            elif mapa[i][j] == 7:
                x = 95 + (j) * 30
                y = 65 + (i) * 30
                parede = Parede(x,y,assets['inf esquerdo'])
                all_bricks.add(parede)
            elif mapa[i][j] == 11:
                x = 95 + (j) * 30
                y = 65 + (i) * 30
                parede = Parede(x,y,assets['inf direito'])
                all_bricks.add(parede)
            elif mapa[i][j] == 10:
                x = 95 + (j) * 30
                y = 65 + (i) * 30
                parede = Parede(x,y,assets['reto'])
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
    state = JOGANDO

    #loop principal
    while state != ACABOU:
        clock.tick(FPS)
        #Trata eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = ACABOU
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
        if state == JOGANDO:
            encostou = pygame.sprite.spritecollide(player,all_monsters, False, pygame.sprite.collide_mask)
            if len(encostou) > 0:
                player.kill()
                #vidas -= 1
                state = ACABOU
        
        if state == JOGANDO:
            encosta = pygame.sprite.spritecollide(player, all_elixir, True, pygame.sprite.collide_mask)

                #print(encostar)

        #Gera saídas
        janela.fill((94, 75, 85))
        cor = (0,0,0)
        pygame.draw.rect(janela,cor,(20,65,60,180))
        #janela.blit(assets['parede'],(80,40))   94, 75, 85

        janela.blit(assets['vida'], (30,70))

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

state = INIT
while state != QUIT:
    if state == INIT:
        state = inicial_screen(janela)
    elif state == GAME:
        state = game_screen(janela)
    else:
        state = QUIT

#finalização
pygame.quit()


