# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from config import *
from classes import *
from sys import exit


#pygame.init()

def quit_game(): #função que fecha o jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

scroll_speed = 1
clock = pygame.time.Clock()

def main():


    run = True
    ground = pygame.sprite.Group()
    #nuvem = pygame.sprite.Group()
    x_inicial, y_inicial = 0, 500
    ground.add(Chao(x_inicial, y_inicial))

    while run:
        #fecha o jogo
        quit_game()

       

        #reset frame
        screen.fill((0, 0, 0))

        

        #fundo de tela
        screen.blit(fundo_blur_img, (0, 0)) #recebe dois argumentos: uma imagem e as coordenadas

        # Tiago aparece 
        tiago = pygame.sprite.GroupSingle()
        tiago.add(Tiago())

        #spawn chao
        if len(ground) <= 2:
            ground.add(Chao(WIDTH, y_inicial))

        # usuario 
        usuario = pygame.key.get_pressed()

        #desenha chao e tiago
        ground.draw(screen)
        tiago.draw(screen)

        #atualiza chao e tiago
        ground.update()
        tiago.update(usuario) 


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