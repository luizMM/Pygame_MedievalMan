import pygame

mapa = [
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4]
    [3, 8, 8, 8, 8, 8, 0, 0, 8, 8, 8, 8, 8, 2]
    [3, 8, 0, 0, 0, 8, 0, 0, 8, 0, 0, 0, 8, 2]
    [3, 9, 0, 0, 0, 8, 0, 0, 8, 0, 0, 0, 9, 2]
    [3, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 2]
    [3, 8, 1, 1, 8, 1, 1, 1, 1, 8, 1, 1, 8, 2]
    [3, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 2]
    [3, 8, 5, 4, 8, 0, 8, 8, 0, 8, 5, 4, 8, 2]
    [3, 8, 7, 6, 8, 0, 8, 8, 0, 8, 7, 6, 8, 2]
    [3, 8, 8, 8, 8, 0, 8, 8, 0, 8, 8, 8, 8, 2]
    [3, 8, 0, 0, 8, 0, 0, 0, 0, 8, 0, 0, 8, 2]
    [3, 8, 0, 0, 8, 8, 8, 8, 8, 8, 0, 0, 8, 2]
    [3, 8, 0, 0, 8, 1, 1, 1, 1, 8, 0, 0, 8, 2]
    [3, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 2]
    [3, 4, 8, 0, 8, 7, 0, 0, 6, 8, 0, 8, 5, 2]
    [3, 2, 8, 1, 8, 8, 8, 8, 8, 8, 1, 8, 3, 2]
    [3, 2, 9, 8, 8, 5, 1, 1, 4, 8, 8, 9, 3, 2]
    [7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6]
]

# def partes_mapa():
#     partes = {}
#     #0
#     partes['parte_cima'] = pygame.image.load('assets/img/parte_cima-1.png.png').convert()
#     #1
#     partes['parte_baixo'] = pygame.image.load('assets/img/parte_baixo-1.png.png').convert()
#     #2
#     partes['lateral_direita'] = pygame.image.load('assets/img/lateral_direita-1.png.png').convert()
#     #3
#     partes['lateral_esquerda'] = pygame.image.load('assets/img/lateral_esquerda-1.png.png').convert()
#     #4
#     partes['canto_superior_direito'] = pygame.image.load('assets/img/canto_superior_direito-1.png.png').convert_alpha()
#     #5
#     partes['canto_superior_esquerdo'] = pygame.image.load('assets/img/canto_superior_esquerdo-1.png.png').convert_alpha()
#     #6
#     partes['canto_inferior_direito'] = pygame.image.load('assets/img/canto_inferior_direito-1.png.png').convert_alpha()
#     #7
#     partes['canto_inferior_esquerdo'] = pygame.image.load('assets/img/canto_inferior_esquerdo-1.png.png').convert()
      #8 moeda
      #9 elixir

#     def render_mapa():
#         for linha in mapa:
#             for coluna in linha:
#                 if mapa[linha][coluna] == 0:
#                     mapa[linha][coluna] = partes['parte_cima']
