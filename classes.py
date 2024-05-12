#definicao das classes do jogo 
from typing import Any
import pygame 
from os import path 
from config import *


scroll_speed = 1

class Tiago (pygame.sprite.Sprite): 
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(personagem, (65, 65))
        self.rect = self.image.get_rect()
        self.rect.center = pos_inic_tiago
        self.vel = 0
        self.flap = False


    def update(self, usuario):
        # Gravidade e pulo
        self.vel += 0.5
        if self.vel > 7:
            self.vel = 7
        if self.rect.y < 500:
            self.rect.y += int(self.vel)
        if self.vel == 0:
            self.pulo = False

        # Rotaciona Tiago
        self.image = pygame.transform.rotate(self.image, self.vel * -7)

        # Usuário
        if usuario[pygame.K_SPACE] and not self.pulo and self.rect.y > 0:
            self.pulo = True
            self.vel = -7




class Chao(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = ground_img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def update(self):
        #mexe o chão
        self.rect.x -= scroll_speed
        if self.rect.x <= -WIDTH:
            self.kill()

