import pygame
import random
from os import path
from config import *
BLACK = (0,0,0) # Cor preta

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Flappy Tiago")


# Background da página inicial
imagem = pygame.image.load(path.join(IMG_DIR, 'tela_inicio.JPEG'))
DEFAULT_IMAGE_SIZE = (WIDTH, HEIGHT)
imagem = pygame.transform.scale(imagem, DEFAULT_IMAGE_SIZE)

background = imagem.convert()
background_rect = background.get_rect()


# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Draw / render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()