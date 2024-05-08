import pygame
from os import path

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'imagens')
SND_DIR = path.join(path.dirname(__file__), 'imagens')
FNT_DIR = path.join(path.dirname(__file__), 'imagens')

scroll_speed = 1

WIDTH = 1200 # Largura da tela 
HEIGHT = 700 # Altura da tela
FPS = 60 # Frames por segundo
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2

#imagens
fundo_blur_img = pygame.image.load("Jogo_Grupo4_1B/imagens/fundo_blur.JPEG") 
coqueiro_img = pygame.image.load("Jogo_Grupo4_1B/imagens/coqueiro.PNG")
nuvem_img = pygame.image.load("Jogo_Grupo4_1B/imagens/nuvem.PNG")
tela_inicio_img = pygame.image.load("Jogo_Grupo4_1B/imagens/tela_inicio.JPEG")   