import sys, pygame
pygame.init()

size = width, height = 1020 , 550 

screen = pygame.display.set_mode(size)

menu1 = pygame.image.load("menu1.jpg")
instrucoes1 = pygame.image.load("instrucoes1.jpg")
opcoes1 = pygame.image.load("1.jpg")
creditos = pygame.image.load("creditos.jpg")

tela = menu1

def updateScreen(menu1):
    screen.blit(menu1, (0, 0))
    pygame.display.update()
    
while 1:
    x, y = pygame.mouse.get_pos()
    print('{} {}'.format(x,y))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #Processamento do Menu
        if  event.type == pygame.MOUSEBUTTONDOWN:
            #Posicao do Start
           # if(x > 114  and x < 314 and y > 113 and y < 213):
           #    screen.blit(tela3, (0,0))
           #     pygame.display.flip()
           #     pygame.time.wait(10000)
           
            #Posicao de Instrucoes
            if(x > 731  and x < 996 and y > 351 and y < 403):
               tela = instrucoes1
               updateScreen(tela)
               
               if(x > 11  and x < 66 and y > 472 and y < 541):
                    tela = menu1
                    updateScreen(tela)
               
            #Posicao do Opcao
            if(x > 732  and x < 994 and y > 413 and y < 466):
               tela = opcoes1
               updateScreen(tela)
               
               if(x > 724  and x < 976 and y > 292 and y < 345):
                    tela = creditos
                    updateScreen(tela)
               if(x > 724  and x < 981 and y > 483 and y < 534):
                    tela = menu1
                    updateScreen(tela)
            #Posicao do Sair
            if(x > 731  and x < 994 and y > 476 and y < 529):
                 pygame.quit()
                 sys.exit()
                
            
    updateScreen(tela)
