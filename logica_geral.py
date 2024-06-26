# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from config import *
from classes import *
from sys import exit
import random 
from assets import load_assets

pygame.mixer.init()

run = True
fim_de_jogo = True
score = 0

pygame.init()

def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

def main():

    assets = load_assets()

    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    ts = pygame.sprite.GroupSingle()
    ground = pygame.sprite.Group()
    #nuvem = pygame.sprite.Group()
    x_inicial, y_inicial = 0, 500
    chao = Chao(assets, x_inicial, y_inicial)
    all_sprites.add(chao)
    ground.add(chao)

    start_time = pygame.time.get_ticks() 
    coqueiros = pygame.sprite.Group()
    
    # Inicializa Tiago
    tiago = Tiago(assets)
    all_sprites.add(tiago)
    ts.add(tiago)

    run = True
    coqueiro_timer = 0

    #screen = pygame.display.set_mode((WIDTH, HEIGHT))
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
    game_over = pygame.image.load("imagens/game_over.JPG")
    game_over = pygame.transform.scale(game_over, (WIDTH, HEIGHT))
    
    general_scroll_speed = min_scroll_speed
    jump_level = 2
    time = 0
    score = 0

    pygame.mixer.music.load("sound/arere.mp3")
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play(loops=-1)



    while run:

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


        # alocando coqueiros

        if coqueiro_timer <= 0 and tiago.vivo:
            x_top, x_bottom = 550, 550
            y_top = random.randint(-650,-560)
            y_bottom = y_top + 100 + coqueiro_img.get_height()
            cima = coqueiro(x_bottom, y_bottom, load_assets()['nuvem'])
            baixo = coqueiro(x_top, chao.rect.top, random.choice(coqueiros_img))
            all_sprites.add(cima)
            all_sprites.add(baixo)
            # coqueiros.add(cima)
            coqueiros.add(baixo) 
            coqueiros.add(cima)
            # print (len(coqueiros))
            coqueiro_timer = 100 
        coqueiro_timer -= 1 
        #time += 1
        
        #if time % 120 == 0 and score % jump_level == 0:
        #    time = 0
        #    if general_scroll_speed < 8:
        #        general_scroll_speed *= 1.1
        #        soma += coqueiro_timer*0.1

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
        for c in coqueiros:
            c.scroll_speed = int(general_scroll_speed)


        #colisao
        colisao_coqueiro = pygame.sprite.spritecollide(ts.sprites()[0], coqueiros, False)
        colisao_chao = pygame.sprite.spritecollide(ts.sprites()[0], ground, False)
        if colisao_chao or colisao_coqueiro:
            tiago.vivo = False
            if colisao_chao:
                screen.blit(tela_inicio_img, (WIDTH // 2 - tela_inicio_img.get_width() // 2,
                                              HEIGHT // 2 - tela_inicio_img.get_height() // 2))
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            score = 0
                            break
            pygame.mixer.music.stop()
                        


        #fundo de tela
        screen.blit(fundo_blur_img, (0, 0)) #recebe dois argumentos: uma imagem e as coordenadas

        #desenha chao,tiago e coqueiros
        all_sprites.draw(screen)

        #score
        score_text = font.render(f'Score: {score/2:.0f}', True, pygame.Color(255, 255, 0))
        screen.blit(score_text, (20, 20))


        if tiago.vivo == False: 
            score = 0 
            # while tiago.rect.bottom != chao.rect.top: 
                # tiago.vel += 1
            
            screen.blit(game_over, (0, 0))
            clock.tick(FPS)
            pygame.display.update()
    
        clock.tick(FPS)
        pygame.display.update()


#pygame.init()

#main()

def menu():
    global fim_de_jogo

    while fim_de_jogo:
        quit_game()
            

        #tela inicial
        screen.blit(load_assets()['tela_inicio'], (0, 0))

        #user input
        user_input = pygame.key.get_pressed()
        if user_input[pygame.K_SPACE]:
            main()

        pygame.display.update()

menu()

#pygame.init()
#pygame.mixer.init()

# ----- Gera tela principal
#window = pygame.display.set_mode((WIDTH, HEIGHT))
#pygame.display.set_caption('Flappy Tiago')

#game_screen(window)

# ===== Finalização =====
#pygame.quit()  # Função do PyGame que finaliza os recursos utilizados