# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from config import *
from classes import *
from sys import exit
import random 
from assets import load_assets

score = 0
def main():
    global score

    assets = load_assets()

    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()

    ground = pygame.sprite.Group()
    #nuvem = pygame.sprite.Group()
    x_inicial, y_inicial = 0, 500
    chao = Chao(assets, x_inicial, y_inicial)
    all_sprites.add(chao)
    ground.add(chao)

     
    coqueiros = pygame.sprite.Group()
    
    # Inicializa Tiago
    tiago = Tiago(assets)
    all_sprites.add(tiago)

    run = True
    coqueiro_timer = 0

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    font = pygame.font.SysFont(None,26) # fonte do score


    #imagens
    fundo_blur_img = pygame.image.load("imagens/fundo_blur.JPEG") 
    coqueiro_img = pygame.image.load("imagens/coqueiro.PNG")
    coqueiros_img = []
    for _ in range(10):
        coqueiros_img.append(pygame.transform.scale(coqueiro_img, (80, 200 + random.randint(0, 50))))
    nuvem_img = pygame.image.load("imagens/nuvem.PNG")
    nuvem_img = pygame.transform.scale(nuvem_img, (175, 200))
    tela_inicio_img = pygame.image.load("imagens/tela_inicio.JPEG")   
    chao_img = pygame.image.load("imagens/chao.JPEG")
    personagem = pygame.image.load("imagens/personagem.PNG") 
    ground_img = pygame.image.load("imagens/ground.PNG") 

    while run:
        #fecha o jogo

        #reset frame
        screen.fill((0, 0, 0))


        # usuario 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and tiago.vivo:
                    tiago.pular()

        
        if len(ground) < 2:
            chao = Chao(assets, WIDTH, y_inicial)
            all_sprites.add(chao)
            ground.add(chao)


        hits = pygame.sprite.spritecollide(tiago, ground, False, pygame.sprite.collide_mask)
        if len(hits) > 0:
            tiago.rect.bottom = chao.rect.top

        if tiago.rect.top < 0:
            tiago.rect.top = 0

        # configurando coqueiros

       

        # alocando coqueiros

        if coqueiro_timer <= 0 and tiago.vivo:
            x_top, x_bottom = 550, 550
            y_top = random.randint(-650,-550)
            y_bottom = y_top + 100 + coqueiro_img.get_height()
            cima = coqueiro(x_bottom, y_bottom, load_assets()['nuvem'])
            baixo = coqueiro(x_top, chao.rect.top, random.choice(coqueiros_img))
            all_sprites.add(cima)
            all_sprites.add(baixo)
            # coqueiros.add(cima)
            coqueiros.add(baixo)
            # print (len(coqueiros))
            coqueiro_timer = 100 
            if score >= 2: 
                scroll_speed = 4
        coqueiro_timer -= 1 
        


        # conta ponto
        # score
        i = 0
        for c in coqueiros:
            i += 1 
            if not c.passou and c.rect.x <= 125:
                c.passou = True
                score += 1




        #atualiza chao, tiago e coqueiros
        all_sprites.update()

        #fundo de tela
        screen.blit(fundo_blur_img, (0, 0)) #recebe dois argumentos: uma imagem e as coordenadas

        #desenha chao,tiago e coqueiros
        all_sprites.draw(screen)

        #score
        score_text = font.render('Score: ' + str(score), True, pygame.Color(255, 255, 0))
        screen.blit(score_text, (20, 20))

        
        clock.tick(FPS)
        pygame.display.update()

pygame.init()

main()



#pygame.init()
#pygame.mixer.init()

# ----- Gera tela principal
#window = pygame.display.set_mode((WIDTH, HEIGHT))
#pygame.display.set_caption('Flappy Tiago')

#game_screen(window)

# ===== Finalização =====
#pygame.quit()  # Função do PyGame que finaliza os recursos utilizados