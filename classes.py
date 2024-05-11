#definicao das classes do jogo 
from typing import Any
import pygame 
from os import path 
from config import *

pos_inic_tiago = (100, 250)
scroll_speed = 1

class tiago (pygame.sprite.Sprite): 
    def __init__(self): 
        pygame.sprite.Sprite.__init__(self)
        self.image = personagem 
        self.rect = self.image.get_rect() 
        self.rect.center = pos_inic_tiago 

    def update(self): 
        self.vel += 0.5 
        if self.vel < 500: 
            self.rect.y += int(self.vel)
        if self.vel == 0: 
            self.flap = False 

        # if user_input[pygame.K_SPACE] and not self.flap and self.rect.y > 0: 
            # self.flap = True 

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

