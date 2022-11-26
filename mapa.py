
mapa = [
    [ 6, 2, 2, 2, 2, 2, 5, 6, 2, 2, 2, 2, 2, 5],
    [10, 8, 8, 8, 8, 8,10,10, 8, 8, 8, 8, 8,10],
    [10, 8, 6, 2, 5, 8,10,10, 8, 6, 2, 5, 8,10],
    [10, 9, 7, 2,11, 8, 7,11, 8, 7, 2,11, 9,10],
    [10, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8,10],
    [10, 8, 3, 4, 8, 3, 2, 2, 4, 8, 3, 4, 8,10],
    [10, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8,10],
    [10, 8, 6, 5, 8, 0,19,19, 0, 8, 6, 5, 8,10],
    [10, 8, 7,11, 8,10,19,19,10, 8, 7,11, 8,10],
    [10, 8, 8, 8, 8,10,19,19,10, 8, 8, 8, 8,10],
    [10, 8, 6, 5, 8, 7, 2, 2,11, 8, 6, 5, 8,10],
    [10, 8,10,10, 8, 8, 8, 8, 8, 8,10,10, 8,10],
    [10, 8, 7,11, 8, 3, 2, 2, 4, 8, 7,11, 8,10],
    [10, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8,10],
    [ 7, 5, 8, 0, 8, 3, 2, 2, 4, 8, 0, 8, 6,10],
    [19,10, 8, 1, 8, 8,19,19, 8, 8, 1, 8,10,19],
    [19,10, 9, 8, 8, 6, 2, 2, 5, 8, 8, 9,10,19],
    [19, 7, 2, 2, 2,11,19,19, 7, 2, 2, 2,11,19],
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
