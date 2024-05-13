# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from config import *
from classes import *
from sys import exit


#pygame.init()


def main():
    scroll_speed = 1
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()

    ground = pygame.sprite.Group()
    #nuvem = pygame.sprite.Group()
    x_inicial, y_inicial = 0, 500
    chao = Chao(x_inicial, y_inicial)
    all_sprites.add(chao)
    ground.add(chao)

    # Inicializa Tiago
    tiago = Tiago()
    all_sprites.add(tiago)

    run = True

    while run:
        #fecha o jogo

        #reset frame
        screen.fill((0, 0, 0))


        # usuario 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    tiago.pular()

        
        if len(ground) < 2:
            chao = Chao(WIDTH, y_inicial)
            all_sprites.add(chao)
            ground.add(chao)


        hits = pygame.sprite.spritecollide(tiago, ground, False, pygame.sprite.collide_mask)
        if len(hits) > 0:
            tiago.rect.bottom = chao.rect.top

        if tiago.rect.top < 0:
            tiago.rect.top = 0


        #atualiza chao e tiago
        all_sprites.update()

        #fundo de tela
        screen.blit(fundo_blur_img, (0, 0)) #recebe dois argumentos: uma imagem e as coordenadas

        #desenha chao e tiago
        all_sprites.draw(screen)


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