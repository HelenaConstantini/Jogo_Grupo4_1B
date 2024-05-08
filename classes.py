#definicao das classes do jogo 
import pygame 
from os import path 
import config 

pos_inic_tiago = (100, 250)
personagem = pygame.image.load("imagens/personagem.PNG") 

class tiago (pygame.sprite.Sprite): 
    def __init__(self): 
        pygame.sprite.Sprite.__init__(self)
        self.image = personagem 
        self.rect = self.imagem.get_rect() 
        self.rect.center = pos_inic_tiago 

    def update(self): 
        self.vel += 0.5 
        if self.vel < 500: 
            self.rect.y += int(self.vel)
        if self.vel == 0: 
            self.flap = False 

        # if user_input[pygame.K_SPACE] and not self.flap and self.rect.y > 0: 
            # self.flap = True 



# class coqueiro (pygame.sprite.Sprite):


