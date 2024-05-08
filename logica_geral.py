# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from config import *
from classes import *
from sys import exit


pygame.init()

def quit_game(): #função que fecha o jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


clock = pygame.time.Clock()

def main():

    run = True
    coqueiro = pygame.sprite.Group()
    nuvem = pygame.sprite.Group()
    x_inicial, y_inicial = 0, 500
    coqueiro.add(Chao(x_inicial, y_inicial))

    while run:
        #fecha o jogo
        quit_game()

        #reset frame
        screen.fill((0, 0, 0))

        #desenha coqueiros, nuvens e tiago
        coqueiro.draw(screen)
        nuvem.draw(screen)

        #atualiza coqueiros, nuvens e tiago
        coqueiro.update()

        #fundo de tela
        screen.blit(fundo_blur_img, (0, 0)) #recebe dois argumentos: uma imagem e as coordenadas

        clock.tick(FPS)
        pygame.display.update()

main()



#pygame.init()
#pygame.mixer.init()

# ----- Gera tela principal
#window = pygame.display.set_mode((WIDTH, HEIGHT))
#pygame.display.set_caption('Flappy Tiago')

#game_screen(window)

# ===== Finalização =====
#pygame.quit()  # Função do PyGame que finaliza os recursos utilizados