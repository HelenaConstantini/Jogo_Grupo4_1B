import pygame
from os import path
import random

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'imagens')
SND_DIR = path.join(path.dirname(__file__), 'imagens')
FNT_DIR = path.join(path.dirname(__file__), 'imagens')



WIDTH = 551 # Largura da tela 
HEIGHT = 600 # Altura da tela
FPS = 60 # Frames por segundo

scroll_speed2 = 6
scroll_speed = 3
pos_inic_tiago = (100, 250) # Posição spawn Tiago 

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2

