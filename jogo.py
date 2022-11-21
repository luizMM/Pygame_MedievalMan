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

#Telas principal do jogo
janela = pygame.display.set_mode((TELA_WIDTH,TELA_HEIGHT))
pygame.display.set_caption('Medieval_man')

#assets
def load_assets():
    assets = {}
    assets['background'] = pygame.image.load('assets/img/Mapa v1-1.png.png').convert_alpha()
    assets['background'] = pygame.transform.scale(assets['background'],(L_MAPA,C_MAPA))
    assets['player'] = pygame.image.load('assets/img/cavaleiro 2-1.png.png').convert_alpha()
    assets['player'] = pygame.transform.scale(assets['player'],(PLAYER_WIDTH,PLAYER_HEIGHT))
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
                        player.speedy -= 8
                    if event.key == pygame.K_DOWN:
                        player.speedy += 8
                    if event.key == pygame.K_LEFT:
                        player.speedx -= 8
                    if event.key == pygame.K_RIGHT:
                        player.speedx += 8
                #verifica se soltou a tecla
                if event.type == pygame.KEYUP:
                    if event.key in key_downs and key_downs[event.key]:
                        if event.key == pygame.K_UP:
                            player.speedy += 8
                        if event.key == pygame.K_DOWN:
                            player.speedy -= 8
                        if event.key == pygame.K_LEFT:
                            player.speedx += 8
                        if event.key == pygame.K_RIGHT:
                            player.speedx -= 8
        #Atualiza posição do personagem
        all_sprites.update()

        #Gera saídas
        janela.fill((0,0,0))
        janela.blit(assets['background'],(80,0))
        all_sprites.draw(janela)

        pygame.display.update()
game_screen(janela)
#finalização
pygame.quit()
