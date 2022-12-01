#importa pacotes
#inicialização
import pygame
from mapa import mapa
import random
from config import *
from assets import *
from inicial_screen import inicial_screen
from game_screen import game_screen
from game_over_screen import game_over_screen
from classes import Player, Zombi, Vampiro, Esqueleto, Demonio, Parede, Moeda, Elixir
#from inicial_screen import inicial_screen

pygame.init()
pygame.mixer.init()

#janela e nome do jogo
janela = pygame.display.set_mode((TELA_WIDTH,TELA_HEIGHT))
pygame.display.set_caption('Medieval_man')

state = INIT
while state != QUIT:
    if state == INIT:
        state = inicial_screen(janela)
    elif state == GAME:
        state = game_screen(janela)
    elif state == OVER:
        state = game_over_screen(janela)
    else:
        state = QUIT

#finalização
pygame.quit()


