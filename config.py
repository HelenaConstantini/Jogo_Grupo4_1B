#coloquei medidas aleatorias
from os import path

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'imagens')
SND_DIR = path.join(path.dirname(__file__), 'imagens')
FNT_DIR = path.join(path.dirname(__file__), 'imagens')


WIDTH = 900 # Largura da tela 
HEIGHT = 700 # Altura da tela
FPS = 60 # Frames por segundo


# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2
