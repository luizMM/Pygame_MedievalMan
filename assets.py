import pygame
import os
from config import PLAYER_HEIGHT,PLAYER_WIDTH

def Assets():
    assets = {}
    assets['tela_inicio'] = pygame.image.load('assets/img/tela_inicial_jogo.png').convert()
    assets['player'] = pygame.image.load('assets/img/cavaleiro 2-1.png').convert_alpha()
    assets['player'] = pygame.transform.scale(assets['player'],(PLAYER_WIDTH,PLAYER_HEIGHT))
