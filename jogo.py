#importa pacotes
#inicialização
import pygame

pygame.init()

#FPS e tamanhos
FPS = 30
TELA_WIDTH = 600
TELA_HEIGHT = 650
L_MAPA = 224*2
C_MAPA = 288*2

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 45

INIT = 0
GAME = 1
QUIT = 2

#Telas principal do jogo
janela = pygame.display.set_mode((TELA_WIDTH,TELA_HEIGHT))
pygame.display.set_caption('Medieval_man')

#assets
def load_assets():
    assets = {}
    assets['mapa'] = pygame.image.load('assets/img/Mapa v2-1.png.png').convert_alpha()
    assets['mapa'] = pygame.transform.scale(assets['background'],(L_MAPA,C_MAPA))
    assets['player'] = pygame.image.load('assets/img/cavaleiro 2-1.png.png').convert_alpha()
    assets['player'] = pygame.transform.scale(assets['player'],(PLAYER_WIDTH,PLAYER_HEIGHT))
    #assets['zombi'] = pygame.image.load('assets/img/Zombi jogo-1png.png').convert_alpha()
    #assets['zombi'] = pygame.transform.scale(assets['zombi'],(PLAYER_WIDTH,PLAYER_HEIGHT))
    return assets

#classe jogador
class Player(pygame.sprite.Sprite):
    def __init__(self,groups,assets):
        pygame.sprite.Sprite.__init__(self)
        #Construção personagem
        self.image = assets['player']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = TELA_WIDTH/2
        self.rect.bottom = TELA_HEIGHT
        self.speedx = 0
        self.speedy = 0
        self.groups = groups
        self.assets = assets
    def update(self):
        #atualiza posição da nave
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        #mantém dento da tela
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > TELA_HEIGHT:
            self.rect.bottom = TELA_HEIGHT
        if self.rect.right > TELA_WIDTH:
            self.rect.right = TELA_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

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

#tela do jogo
def game_screen(janela):
    #clock(fps)
    clock = pygame.time.Clock()

    assets = load_assets()

    all_sprites = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites

    player = Player(groups,assets)
    all_sprites.add(player)

    key_downs = {}

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

        #Gera saídas
        janela.fill((0,0,0))
        janela.blit(assets['mapa'],(80,40))
        all_sprites.draw(janela)

        pygame.display.update()

state = INIT
while state != QUIT:
    if state == INIT:
        inicial_screen(janela)
    elif state == GAME:
        game_screen(janela)
    else:
        state = QUIT


#finalização
pygame.quit()
