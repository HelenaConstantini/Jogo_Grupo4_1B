# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from config import *
import game_screen
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
    while run:
        #fecha o jogo
        quit_game()

        #reset frame
        window.fill((0, 0, 0))

        #fundo de tela
        window.blit(fundo_blur, (0, 0)) #recebe dois argumentos: uma imagem e as coordenadas

        clock.tick(FPS)
        pygame.display.update()

main()










pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Tiago')

game_screen(window)

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados