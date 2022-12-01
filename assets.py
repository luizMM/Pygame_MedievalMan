import pygame
import os
from config import *

MAPA = 'mapa'
MOEDA = 'moeda'
ELIXIR = 'elixir'
DEITADO = 'deitado'
CIMA = 'cima'
BAIXO = 'baixo'
RETO = 'reto'
ESQUERDO = 'esquerdo'
DIREITO = 'direito'
SUP_DIREITO = 'sup direito'
SUP_ESQUERDO = 'sup esquerdo'
INF_DIREITO = 'inf direito'
INF_ESQUERDO = 'inf esquerdo'
SCORE_FONT = 'score_font'

def load_assets():
    assets = {}
    assets[MAPA] = pygame.image.load('assets/img/Mapa v2-1.png-1.png.png').convert_alpha()
    assets[MAPA] = pygame.transform.scale(assets['mapa'],(L_MAPA,C_MAPA))
    assets[SCORE_FONT] = pygame.font.Font('assets/font/PressStart2P.ttf', 28)
    #assets['player'] = pygame.image.load('assets/img/cavaleiro 2-1.png.png').convert_alpha()
    #assets['player'] = pygame.transform.scale(assets['player'],(PLAYER_WIDTH,PLAYER_HEIGHT))
    #assets['vida'] = pygame.image.load('assets/img/Coracao_vida-1.png.png').convert_alpha()
    #assets['vida'] = pygame.transform.scale(assets['vida'],(40,40))
    # assets['zombi'] = pygame.image.load('assets/img/Zombi jogo-1.png.png').convert_alpha()
    # assets['zombi'] = pygame.transform.scale(assets['zombi'],(MONSTER_WIDTH,MONSTER_HEIGHT))
    # assets['esqueleto'] = pygame.image.load('assets/img/Esqueleto jogo-1.png.png').convert_alpha()
    # assets['esqueleto'] = pygame.transform.scale(assets['esqueleto'], (MONSTER_WIDTH,MONSTER_HEIGHT))
    # assets['vampiro'] = pygame.image.load('assets/img/Vampiro jogo-1.png.png').convert_alpha()
    # assets['vampiro'] = pygame.transform.scale(assets['vampiro'], (MONSTER_WIDTH,MONSTER_HEIGHT))
    #assets['demonio'] = pygame.image.load('assets/img/Demonio-1.png.png').convert_alpha()
    #assets['demonio'] = pygame.transform.scale(assets['demonio'], (MONSTER_WIDTH,MONSTER_HEIGHT))

    assets[MOEDA] = pygame.image.load('assets/img/Moeda-1.png.png').convert_alpha()
    assets[MOEDA] = pygame.transform.scale(assets['moeda'], (16,16))
    assets[ELIXIR] = pygame.image.load('assets/img/Pocao poderosa-1.png.png').convert_alpha()
    assets[ELIXIR] = pygame.transform.scale(assets['elixir'], (16,16))

    assets[DEITADO] = pygame.image.load('assets/img/Parte deitada-1.png.png').convert()
    assets[DEITADO] = pygame.transform.scale(assets['deitado'], (30,30))
    assets[CIMA] = pygame.image.load('assets/img/Parte cima-1.png.png').convert()
    assets[CIMA] = pygame.transform.scale(assets['cima'], (30,30))
    assets[BAIXO] = pygame.image.load('assets/img/Parte baixo-1.png.png').convert()
    assets[BAIXO] = pygame.transform.scale(assets['baixo'], (30,30))
    assets[RETO] = pygame.image.load('assets/img/Parte reta-1.png.png').convert()
    assets[RETO] = pygame.transform.scale(assets['reto'], (30,30))
    assets[ESQUERDO] = pygame.image.load('assets/img/Parte esquerda-1.png.png').convert()
    assets[ESQUERDO] = pygame.transform.scale(assets['esquerdo'], (30,30))
    assets[DIREITO] = pygame.image.load('assets/img/Parte direita-1.png.png').convert()
    assets[DIREITO] = pygame.transform.scale(assets['direito'], (30,30))
    assets[SUP_DIREITO] = pygame.image.load('assets/img/canto sup direito-1.png.png').convert()
    assets[SUP_DIREITO] = pygame.transform.scale(assets['sup direito'], (30,30))
    assets[SUP_ESQUERDO] = pygame.image.load('assets/img/canto sup esquerda-1.png.png').convert()
    assets[SUP_ESQUERDO] = pygame.transform.scale(assets['sup esquerdo'], (30,30))
    assets[INF_DIREITO] = pygame.image.load('assets/img/canto inf direito-1.png.png').convert()
    assets[INF_DIREITO] = pygame.transform.scale(assets['inf direito'], (30,30))
    assets[INF_ESQUERDO] = pygame.image.load('assets/img/canto inf esquerdo-1.png.png').convert()
    assets[INF_ESQUERDO] = pygame.transform.scale(assets['inf esquerdo'], (30,30))

    #musica do jogo
    pygame.mixer.music.load('assets/sounds/Medievalman.mp3')
    pygame.mixer.music.set_volume(1)
    return assets
