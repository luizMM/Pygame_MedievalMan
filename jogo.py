import pygame

pygame.init()

FPS = 30
TELA_WIDTH = 600
TELA_HEIGHT = 500
janela = pygame.display.set_mode((TELA_WIDTH,TELA_HEIGHT))
pygame.display.set_caption('Medieval_man')

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 45

def load_assets():
    assets = {}
    #assets['background'] = 
    assets['player'] = pygame.image.load('assets/img/cavaleiro 2-1.png.png').convert_alpha()
    assets['player'] = pygame.transform.scale(assets['player'],(PLAYER_WIDTH,PLAYER_HEIGHT))
    return assets

class Player(pygame.sprite.Sprite):
    def __init__(self,groups,assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['player']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = TELA_WIDTH/2
        self.rect.bottom = TELA_HEIGHT - 10
        self.speedx = 0
        self.speedy = 0
        self.groups = groups
        self.assets = assets
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top > TELA_HEIGHT:
            self.rect.top = TELA_HEIGHT
        if self.rect.bottom < 0:
            self.rect.bottom = 0
        if self.rect.right > TELA_WIDTH:
            self.rect.right = TELA_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

def game_screen(janela):
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

    while state != ACABOU:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = ACABOU
            if state == JOGANDO:
                if event.type == pygame.KEYDOWN:
                    key_downs[event.key] = True
                    if event.key == pygame.K_UP:
                        player.speedy -= 8
                    if event.key == pygame.K_DOWN:
                        player.speedy += 8
                    if event.key == pygame.K_LEFT:
                        player.speedx -= 8
                    if event.key == pygame.K_RIGHT:
                        player.speedx += 8
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
        all_sprites.update()

        janela.fill((255,255,255))
        all_sprites.draw(janela)

        pygame.display.update()
game_screen(janela)

pygame.quit()