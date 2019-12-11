import sys, pygame
pygame.init()

size = width, height = 1020 , 550 

screen = pygame.display.set_mode(size)

menu1 = pygame.image.load("menu1.jpg")
instrucoes1 = pygame.image.load("instrucoes1.jpg")
opcoes1 = pygame.image.load("1.jpg")
creditos = pygame.image.load("creditos.jpg")
teste1 = pygame.image.load("niveis.jpeg")
niveis = pygame.image.load("niveis.jpeg")

ashePuzzle = pygame.image.load("ashe-puzzle.jpeg")
lissandraPuzzle = pygame.image.load("lissandra-puzzle.jpeg")

#Peças Ashe
ashe1 = pygame.image.load("ashe1.png")
ashe2 = pygame.image.load("ashe2.png")
ashe3 = pygame.image.load("ashe3.png")
ashe4 = pygame.image.load("ashe4.png")

#Peças Lissandra
lissandra1 = pygame.image.load("lissandra1.png")
lissandra2 = pygame.image.load("lissandra2.png")
lissandra3 = pygame.image.load("lissandra3.png")
lissandra4 = pygame.image.load("lissandra4.png")
lissandra5 = pygame.image.load("lissandra5.png")
lissandra6 = pygame.image.load("lissandra6.png")
lissandra7 = pygame.image.load("lissandra7.png")
lissandra8 = pygame.image.load("lissandra8.png")
lissandra9 = pygame.image.load("lissandra9.png")

asheposicaocorreta = [0,0,0,0]
asheP1 = x , y = 354, 105
asheP2 = x , y = 499, 103
asheP3 = x , y = 352, 253
asheP4 = x , y = 500, 251

lissandraposicaocorreta = [0,0,0,0,0,0,0,0,0]
lissandraP1 = x , y = 360, 108
lissandraP2 = x , y = 455, 108
lissandraP3 = x , y = 550, 107
lissandraP4 = x , y = 359, 203
lissandraP5 = x , y = 454, 204
lissandraP6 = x , y = 550, 203
lissandraP7 = x , y = 359, 299
lissandraP8 = x , y = 455, 300
lissandraP9 = x , y = 551, 300

tela = menu1

mouseclick = pygame.mixer.music.load("Lissandra.mpeg")
pygame.mixer.music.play(0,0)

menuInicial = True
instrucoes = False
opcao = False
telaDeCreditos = False
jogar = False
niveisTela = False
asheTela = False
lissandraTela = False
tela1 = False


segundoclique = False
primeiroclique = True
naoposicionou = True
peca = 'oi'
pos = 1

def updateScreen(menu1):
    screen.blit(menu1, (0, 0))
    if(asheP1):
        pygame.display.update()
    elif(asheP2):
        pygame.display.update()
    elif(asheP3):
        pygame.display.update()
    elif(asheP4):
        pygame.display.update()
    elif(lissandra1):
        pygame.display.update()
    elif(lissandra2):
        pygame.display.update()
    elif(lissandra3):
        pygame.display.update()
    elif(lissandra4):
        pygame.display.update()
    elif(lissandra5):
        pygame.display.update()
    elif(lissandra6):
        pygame.display.update()
    elif(lissandra7):
        pygame.display.update()
    elif(lissandra8):
        pygame.display.update()
    elif(lissandra9):
        pygame.display.update()
        
def movePeca(peca, pos):
    #Primeira posicao do quebra-cabeca
    if(pos == 1):        
        if(peca == 'ashe1'):
            updateScreen(ashePuzzle)
            soposicaocorreta[0] = 1
            pygame.display.update()
    #Segunda posicao do quebra-cabeca         
    if(pos == 2):
        if(peca == 'ashe2'):
            updateScreen(ashePuzzle)
            soposicaocorreta[1] = 1
            pygame.display.update()
    #Terceira posicao do quebra-cabeca         
    if(pos == 3):
        if(peca == 'ashe3'):
            updateScreen(ashePuzzle)
            soposicaocorreta[2] = 1
            pygame.display.update()
    #Quarta posicao do quebra-cabeca
    if(pos == 4):
        if(peca == 'ashe4'):
            updateScreen(ashePuzzle)
            soposicaocorreta[3] = 1
            pygame.display.update()

updateScreen(tela)
c1x = 0
c1y = 0
c2x = 0
c2y = 0


def movePecaLissandra(peca, pos):
    #Primeira posicao do quebra-cabeca
    if(pos == 1):
        
        if(peca == 'lissandra1'):
            lissandraposicaocorreta[0]=1
            pygame.display.update()
        #elif
        #   pygame.music.play()
    if(pos == 2):
        if(peca == 'lissandra2'):
            lissandraposicaocorreta[1]=1
            pygame.display.update()
         #elif
         #   pygame.music.play()
    if(pos == 3):
        if(peca == 'lissandra3'):
            lissandraposicaocorreta[2]=1
            pygame.display.update()
         #elif
         #  pygame.music.play()
    if(pos == 4):
        if(peca == 'lissandra4'):
            lissandraposicaocorreta[3]=1
            pygame.display.update()
         #elif
         #  pygame.music.play()
    if(pos == 5):
        if(peca == 'lissandra5'):
            lissandraposicaocorreta[4]=1
            pygame.display.update()
    if(pos == 6):
        if(peca == 'lissandra6'):
            lissandraposicaocorreta[5]=1
            pygame.display.update()
    if(pos == 7):
        if(peca == 'lissandra7'):
            lissandraposicaocorreta[6]=1
            pygame.display.update()
    if(pos == 8):
        if(peca == 'lissandra8'):
            lissandraposicaocorreta[7]=1
            pygame.display.update()
    if(pos == 9):
        if(peca == 'lissandra9'):
            lissandraposicaocorreta[8]=1
            pygame.display.update()
updateScreen(tela)
c1x = 0
c1y = 0
c2x = 0
c2y = 0
            
while 1:
    #Exibe posicao do mouse
    x, y = pygame.mouse.get_pos()
    print('{} {}'.format(x,y))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #Processamento do Menu
        if  event.type == pygame.MOUSEBUTTONDOWN:
            clicou = True
            #Posicao do Clique
            if(jogar and primeiroclique and clicou):
                c1x = x
                c1y = y
                primeiroclique = False
                segundoclique = True
                clicou = False
            if(jogar and segundoclique and clicou):
                c2x = x
                c2y = y
                segundoclique = False
                primeiroclique = True
                
            #Posicao do botao Jogar    
            if(x > 730  and x < 993 and y > 288 and y < 340 and menuInicial):
               size = width, height = 1024 , 547 
               screen = pygame.display.set_mode(size)
               menuInicial = False
               niveisTela = True
               tela = teste1
               updateScreen(tela)
            #Posicao do botao facil
            if(x > 656  and x < 944 and y > 339 and y < 402 and niveisTela):
               size = width, height = 1024 , 547 
               screen = pygame.display.set_mode(size)
               niveisTela = False
               asheTela = True
               tela = ashePuzzle
               updateScreen(tela)
               
            if(asheTela):
                if(naoposicionou):
                    screen.blit(ashe1, (691, 19))
                    screen.blit(ashe2, (834, 93))
                    screen.blit(ashe3, (675, 215))
                    screen.blit(ashe4, (846, 287))
                    pygame.display.update()
                    naoposicionou = False
                                      
                #Define peca

                if(c1x > 691 and c1x < 833 and c1y > 19 and c1y < 171 and segundoclique):
                     peca = 'ashe4' 

                if(c1x > 834 and c1x < 1021 and c1y > 93 and c1y < 244 and segundoclique):
                     peca = 'ashe3' 
                   
                if(c1x > 675 and c1x < 821 and c1y > 215 and c1y < 357 and segundoclique):
                     peca = 'ashe1'
                   
                if(c1x > 846 and c1x < 1027 and c1y > 287 and c1y < 468 and segundoclique):
                     peca = 'ashe2'                 

                #Define posicao     
                if(c2x > 354 and c2x < 498 and c2y > 105 and c2y < 250 and primeiroclique):
                     pos = 1
                
                if(c2x > 499 and c2x < 644 and c2y > 103 and c2y < 247 and primeiroclique):
                     pos = 2
               
                if(c2x > 352 and c2x < 499 and c2y > 253 and c2y < 397 and primeiroclique):
                     pos = 3
             
                if(c2x > 500 and c2x < 646 and c2y > 251 and c2y < 396 and primeiroclique):
                     pos = 4
                print(peca)
                print(pos)
                print(c1x, c1y)
                print(c2x, c2y)
                if(primeiroclique):
                    movePeca(peca,pos)
                                      
            #Botão de voltar de tela nivel facil   
            if(x > 11  and x < 66 and y > 472 and y < 541 and asheTela):
               asheTela = False
               niveisTela = True
               tela = niveis
               updateScreen(tela)
            #Posicao do botao dificil  
            if(x > 656  and x < 944 and y > 407 and y < 471 and niveisTela):
               size = width, height = 1024 , 547 
               screen = pygame.display.set_mode(size)
               niveisTela = False
               lissandraTela = True
               tela = lissandraPuzzle
               updateScreen(tela)

               
            #Botão de voltar de tela nivel dificil   
            if(x > 11  and x < 66 and y > 472 and y < 541 and lissandraTela):
               lissandraTela = False
               niveisTela = True
               tela = niveis
               updateScreen(tela)


            if(lissandraTela):
                if(naoposicionou):
                    screen.blit(lissandra1, (691, 19))
                    screen.blit(lissandra2, (834, 93))
                    screen.blit(lissandra3, (675, 215))
                    screen.blit(lissandra4, (846, 287))
                    screen.blit(lissandra5, (846, 287))
                    screen.blit(lissandra6, (846, 287))
                    screen.blit(lissandra7, (846, 287))
                    screen.blit(lissandra8, (846, 287))
                    screen.blit(lissandra9, (846, 287))
                    
                    pygame.display.update()
                    naoposicionou = False
            #Define peca

                if(c1x > 663 and c1x < 759 and c1y > 11 and c1y < 94 and segundoclique):
                     peca = 'lissandra2' 

                if(c1x > 788 and c1x < 864 and c1y > 48 and c1y < 138 and segundoclique):
                     peca = 'lissandra3' 
                   
                if(c1x > 898 and c1x < 1004 and c1y > 21 and c1y < 122 and segundoclique):
                     peca = 'lissandra1'

                if(c1x > 904 and c1x < 1017 and c1y > 161 and c1y < 257 and segundoclique):
                     peca = 'lissandra9'
                     
                if(c1x > 669 and c1x < 754 and c1y > 157 and c1y < 234 and segundoclique):
                     peca = 'lissandra4'
                     
                if(c1x > 787 and c1x < 868 and c1y > 226 and c1y < 318 and segundoclique):
                     peca = 'lissandra6'
                     
                if(c1x > 921 and c1x < 1019 and c1y > 391 and c1y < 461 and segundoclique):
                     peca = 'lissandra8'
                     
                if(c1x > 775 and c1x < 877 and c1y > 386 and c1y < 465 and segundoclique):
                     peca = 'lissandra7'
                     
                if(c1x > 653 and c1x < 754 and c1y > 379 and c1y < 461 and segundoclique):
                     peca = 'lissandra5'
                     
                #Define posicao     
                if(c2x > 360 and c2x < 452 and c2y > 108 and c2y < 202 and primeiroclique):
                     pos = 1
                
                if(c2x > 455 and c2x < 642 and c2y > 107 and c2y < 200 and primeiroclique):
                     pos = 2
               
                if(c2x > 550 and c2x < 642 and c2y > 107 and c2y < 200 and primeiroclique):
                     pos = 3
             
                if(c2x > 359 and c2x < 453 and c2y > 203 and c2y < 297 and primeiroclique):
                     pos = 4
                     
                if(c2x > 454 and c2x < 548 and c2y > 204 and c2y < 298 and primeiroclique):
                     pos = 5
                     
                if(c2x > 550 and c2x < 644 and c2y > 203 and c2y < 297 and primeiroclique):
                     pos = 6
                     
                if(c2x > 359 and c2x < 453 and c2y > 299 and c2y < 392 and primeiroclique):
                     pos = 7
                     
                if(c2x > 455 and c2x < 548 and c2y > 299 and c2y < 392 and primeiroclique):
                     pos = 8
                     
                if(c2x > 551 and c2x < 641 and c2y > 300 and c2y < 393 and primeiroclique):
                     pos = 9
                     
                print(peca)
                print(pos)
                print(c1x, c1y)
                print(c2x, c2y)
                
                if(primeiroclique):
                    movePecaLissandra(peca,pos)

                    
            #Botão de voltar da tela de niveis   
            if(x > 660  and x < 945 and y > 479 and y < 536 and niveisTela):
                menuInicial = True
                niveisTela = False
                #gambiarra
                x=10
                y=20
                tela = menu1
                updateScreen(tela)
               
                
            #Posicao de Instrucoes
            if(x > 731  and x < 996 and y > 351 and y < 403 and menuInicial):
               menuInicial = False
               instrucoes = True
               tela = instrucoes1
               updateScreen(tela)
            #Botão de voltar de instrucoes   
            if(x > 11  and x < 66 and y > 472 and y < 541 and instrucoes):
               menuInicial = True
               instrucoes = False
               tela = menu1
               updateScreen(tela)
               
            #Posicao do Opcao
            if(x > 732  and x < 994 and y > 413 and y < 466 and menuInicial):
               menuInicial = False
               opcao = True
               tela = opcoes1
               updateScreen(tela)
            #Posicao do botão créditos   
            if(x > 724  and x < 976 and y > 292 and y < 345 and opcao):
               opcao = False
               telaDeCreditos = True
               tela = creditos
               updateScreen(tela)
            #Posicao do botão voltar da tela de créditos        
            if(x > 11  and x < 66 and y > 472 and y < 541 and telaDeCreditos):
               telaDeCreditos = False
               opcao = True
               tela = opcoes1
               updateScreen(tela)
               
             #Posicao do voltar da tela de opcoes
            if(x > 731  and x < 994 and y > 476 and y < 529 and opcao):
                menuInicial = True
                opcao = False
                #gambiarra
                x=10
                y=20
                tela = menu1
                updateScreen(tela)
                   
            #Posicao do Sair da tela inicial
            if(x > 731  and x < 994 and y > 476 and y < 529 and menuInicial):
                pygame.quit()
                sys.exit()
                
          



