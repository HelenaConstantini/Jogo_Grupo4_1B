import pygame
from os import path

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'imagens')
SND_DIR = path.join(path.dirname(__file__), 'imagens')
FNT_DIR = path.join(path.dirname(__file__), 'imagens')

scroll_speed = 1

WIDTH = 700 # Largura da tela 
HEIGHT = 600 # Altura da tela
FPS = 60 # Frames por segundo
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2

#imagens
fundo_blur_img = pygame.image.load("imagens/fundo_blur.JPEG") 
coqueiro_img = pygame.image.load("imagens/coqueiro.PNG")
nuvem_img = pygame.image.load("imagens/nuvem.PNG")
tela_inicio_img = pygame.image.load("imagens/tela_inicio.JPEG")   
chao_img = pygame.image.load("imagens/chao.JPEG")
personagem = pygame.image.load("imagens/personagem.PNG") 
ground_img = pygame.image.load("imagens/ground.PNG")