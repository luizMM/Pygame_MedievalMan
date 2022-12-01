import pygame
import random
from config import *
from mapa import mapa
from assets import ELIXIR, MOEDA


class Player(pygame.sprite.Sprite):
    def __init__(self,groups,assets):
        pygame.sprite.Sprite.__init__(self)
        #Construção personagem
        self.animation = []
        self.animation.append(pygame.image.load('assets/img/cavaleiro 2-1.png.png'))
        self.animation.append(pygame.image.load('assets/img/cavaleiro 2-2.png.png'))
        self.frame = 0
        self.image = self.animation[self.frame]
        self.image = pygame.transform.scale(self.image, (PLAYER_WIDTH,PLAYER_HEIGHT))
        
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = TELA_WIDTH/2 + 5
        self.rect.bottom = TELA_HEIGHT - 90
        self.speedx = 0
        self.speedy = 0
        self.groups = groups
        self.assets = assets
    def update(self):
        #animacao jogador
        self.frame += 0.08
        if self.frame >= len(self.animation):
            self.frame = 0
        self.image = self.animation[int(self.frame)]
        self.image = pygame.transform.scale(self.image, (PLAYER_WIDTH,PLAYER_HEIGHT))
        #nova posicao
        bkpx = self.rect.x
        bkpy = self.rect.y
        #atualiza posição do player
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        i = (self.rect.x + (PLAYER_WIDTH//2) - 95) // 30
        j = (self.rect.y + (PLAYER_HEIGHT//2)- 65) // 30
        #ver se as posicoes e maior que o mapa
        if i >= 0 and i < len(mapa[0]) and j >= 0 and j < len(mapa):
            if mapa[j][i] in [0,1,2,3,4,5,6,7,10,11]:
                self.rect.x = bkpx  
                self.rect.y = bkpy
                #print('nao pode mover')
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
        #animação
        self.animation = []
        self.animation.append(pygame.image.load('assets/img/Zombi jogo-1.png.png'))
        self.animation.append(pygame.image.load('assets/img/Zombi jogo-2.png.png'))
        self.frame = 0
        self.image = self.animation[self.frame]

        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = TELA_WIDTH/2 + 15
        self.rect.bottom = TELA_HEIGHT/2
        self.speedx = 0
        self.speedy = 0
        self.groups = groups
        self.assets = assets
    def update(self):
        self.frame += 0.12
        if self.frame >= len(self.animation):
            self.frame = 0
        self.image = self.animation[int(self.frame)]
        self.image = pygame.transform.scale(self.image, (MONSTER_WIDTH,MONSTER_HEIGHT))

        if self.speedx == 0 and self.speedy == 0:
            if random.uniform(0,1) > 0.5:
                self.speedx = 0
                self.speedy = random.randint(-5,5)
            else:
                self.speedx = random.randint(-5,5)
                self.speedy = 0
        bkpx = self.rect.x
        bkpy = self.rect.y
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        i = (self.rect.x + (MONSTER_WIDTH//2) - 95) // 30
        j = (self.rect.y + (MONSTER_HEIGHT//2)- 65) // 30
        if i >= 0 and i < len(mapa[0]) and j >= 0 and j < len(mapa):
            if mapa[j][i] in [0,1,2,3,4,5,6,7,10,11]:
                self.rect.x = bkpx  
                self.rect.y = bkpy
                self.speedx = 0
                self.speedy = 0

class Vampiro(pygame.sprite.Sprite):
    def __init__(self,groups,assets):
        pygame.sprite.Sprite.__init__(self)
        self.animation = []
        self.animation.append(pygame.image.load('assets/img/Vampiro jogo-1.png.png'))
        self.animation.append(pygame.image.load('assets/img/Vampiro jogo-2.png.png'))
        self.frame = 0
        self.image = self.animation[self.frame]
        self.image = pygame.transform.scale(self.image, (MONSTER_WIDTH,MONSTER_HEIGHT))
    
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = TELA_WIDTH/2 - 10
        self.rect.bottom = TELA_HEIGHT/2
        self.speedx = 0
        self.speedy = 0
        self.groups = groups
        self.assets = assets
    def update(self):
        #animacao esqueleto
        self.frame += 0.12
        if self.frame >= len(self.animation):
            self.frame = 0
        self.image = self.animation[int(self.frame)]
        self.image = pygame.transform.scale(self.image, (MONSTER_WIDTH,MONSTER_HEIGHT))
        if self.speedx == 0 and self.speedy == 0:
            if random.uniform(0,1) > 0.5:
                self.speedx = 0
                self.speedy = random.randint(-5,5)
            else:
                self.speedx = random.randint(-5,5)
                self.speedy = 0
        bkpx = self.rect.x
        bkpy = self.rect.y
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        i = (self.rect.x + (MONSTER_WIDTH//2) - 95) // 30
        j = (self.rect.y + (MONSTER_HEIGHT//2)- 65) // 30
        if i >= 0 and i < len(mapa[0]) and j >= 0 and j < len(mapa):
            if mapa[j][i] in [0,1,2,3,4,5,6,7,10,11]:
                self.rect.x = bkpx  
                self.rect.y = bkpy
                self.speedx = 0
                self.speedy = 0

class Esqueleto(pygame.sprite.Sprite):
    def __init__(self,groups,assets):
        pygame.sprite.Sprite.__init__(self)

        self.animation = []
        self.animation.append(pygame.image.load('assets/img/Esqueleto jogo-1.png.png'))
        self.animation.append(pygame.image.load('assets/img/Esqueleto jogo-2.png.png'))
        self.frame = 0
        self.image = self.animation[self.frame]
        self.image = pygame.transform.scale(self.image, (MONSTER_WIDTH,MONSTER_HEIGHT))

        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = TELA_WIDTH/2 - 10
        self.rect.bottom = TELA_HEIGHT/2 + 30
        self.speedx = 0
        self.speedy = 0
        self.groups = groups
        self.assets = assets
    def update(self):
        #animacao do monstro
        self.frame += 0.12
        if self.frame >= len(self.animation):
            self.frame = 0
        self.image = self.animation[int(self.frame)]
        self.image = pygame.transform.scale(self.image, (MONSTER_WIDTH,MONSTER_HEIGHT))

        if self.speedx == 0 and self.speedy == 0:
            if random.uniform(0,1) > 0.5:
                self.speedx = 0
                self.speedy = random.randint(-5,5)
            else:
                self.speedx = random.randint(-5,5)
                self.speedy = 0
        bkpx = self.rect.x
        bkpy = self.rect.y
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        i = (self.rect.x + (MONSTER_WIDTH//2) - 95) // 30
        j = (self.rect.y + (MONSTER_HEIGHT//2)- 65) // 30
        if i >= 0 and i < len(mapa[0]) and j >= 0 and j < len(mapa):
            if mapa[j][i] in [0,1,2,3,4,5,6,7,10,11]:
                self.rect.x = bkpx  
                self.rect.y = bkpy
                self.speedx = 0
                self.speedy = 0

class Demonio(pygame.sprite.Sprite):
    def __init__(self,groups,assets):
        pygame.sprite.Sprite.__init__(self)

        self.animation = []
        self.animation.append(pygame.image.load('assets/img/Demonio-1.png.png'))
        self.animation.append(pygame.image.load('assets/img/Demonio-2.png.png'))
        self.frame = 0
        self.image = self.animation[self.frame]
        self.image = pygame.transform.scale(self.image, (MONSTER_WIDTH,MONSTER_HEIGHT))

        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = TELA_WIDTH/2 + 18
        self.rect.bottom = TELA_HEIGHT/2 + 30
        self.speedx = 0
        self.speedy = 0
        self.groups = groups
        self.assets = assets
    def update(self):
        #animacao do monstro
        self.frame += 0.12
        if self.frame >= len(self.animation):
            self.frame = 0
        self.image = self.animation[int(self.frame)]
        self.image = pygame.transform.scale(self.image, (MONSTER_WIDTH,MONSTER_HEIGHT))

        if self.speedx == 0 and self.speedy == 0:
            if random.uniform(0,1) > 0.5:
                self.speedx = 0
                self.speedy = random.randint(-5,5)
            else:
                self.speedx = random.randint(-5,5)
                self.speedy = 0
        bkpx = self.rect.x
        bkpy = self.rect.y
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        i = (self.rect.x + (MONSTER_WIDTH//2) - 95) // 30
        j = (self.rect.y + (MONSTER_HEIGHT//2)- 65) // 30
        if i >= 0 and i < len(mapa[0]) and j >= 0 and j < len(mapa):
            if mapa[j][i] in [0,1,2,3,4,5,6,7,10,11]:
                self.rect.x = bkpx  
                self.rect.y = bkpy
                self.speedx = 0
                self.speedy = 0

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

        self.image = assets[MOEDA]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Elixir(pygame.sprite.Sprite):
    def __init__(self,x,y,assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[ELIXIR]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y