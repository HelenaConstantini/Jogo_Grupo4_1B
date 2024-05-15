#definicao das classes do jogo 
from typing import Any
import pygame 
from os import path 
from config import *


scroll_speed = 2

class Tiago (pygame.sprite.Sprite): 
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(personagem, (65, 65))
        self.rect = self.image.get_rect()
        self.rect.center = pos_inic_tiago
        self.vel = 5
        self.pulo = False
        self.vivo = True

    def pular(self):
        self.pulo = True
        self.vel += -10


    def update(self):
        if self.vel == 0:
            self.pulo = False

        self.rect.y += int(self.vel)
        # Gravidade e pulo
        self.vel += 0.5
        if self.vel > 5:
            self.vel = 5
        # if self.rect.y < 500:
        #     self.rect.y += int(self.vel)

        # Rotaciona Tiago
        # if self.pulo:
        #     self.image = pygame.transform.rotate(self.image, self.vel * -5)





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



 # coqueiros

class coqueiro(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.bottom = x,y
        
       # fazer os coqueiros se mexer 
    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.x <= -WIDTH:
            self.kill()

