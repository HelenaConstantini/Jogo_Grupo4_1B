import pygame
from config import *

pygame.mixer.init()

#função de carregamento de assets do jogo 
 
def load_assets():
    font = pygame.font.SysFont(None,26) # fonte do score


    #imagens
    fundo_blur_img = pygame.image.load("imagens/fundo_blur.JPEG") 
    coqueiro_img = pygame.image.load("imagens/coqueiro.PNG")
    coqueiros_img = []
    for _ in range(10):
        coqueiros_img.append(pygame.transform.scale(coqueiro_img, (80, 200 + random.randint(0, 50))))
    nuvem_img = pygame.image.load("imagens/nuvem.PNG")
    nuvem_img = pygame.transform.scale(nuvem_img, (75, 75))
    tela_inicio_img = pygame.image.load("imagens/tela_inicio.JPEG")  
    tela_inicio_img = pygame.transform.scale(tela_inicio_img, (550, 600)) 
    chao_img = pygame.image.load("imagens/chao.JPEG")
    personagem = pygame.image.load("imagens/personagem.PNG") 
    personagem = pygame.transform.scale(personagem, (50, 50))
    ground_img = pygame.image.load("imagens/ground.PNG")
    game_over = pygame.image.load("imagens/game_over.JPG")
    musica = pygame.mixer.music.load("sound/arere.mp3")
    return {
        'font': font,
        'ground_img': ground_img,
        'personagem': personagem,
        'nuvem': nuvem_img,
        'tela_inicio': tela_inicio_img,
        'coqueiro': coqueiros_img,
        'fundo_blur': fundo_blur_img,
        'game_over': game_over
    }