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
ashe1 = pygame.image.load("ashe1.jpeg")
ashe2 = pygame.image.load("ashe2.jpeg")
ashe3 = pygame.image.load("ashe3.jpeg")
ashe4 = pygame.image.load("ashe4.jpeg")

#Peças Lissandra
lissandra1 = pygame.image.load("lissandra1.jpeg")
lissandra2 = pygame.image.load("lissandra2.jpeg")
lissandra3 = pygame.image.load("lissandra3.jpeg")
lissandra4 = pygame.image.load("lissandra4.jpeg")
lissandra5 = pygame.image.load("lissandra5.jpeg")
lissandra6 = pygame.image.load("lissandra6.jpeg")
lissandra7 = pygame.image.load("lissandra7.jpeg")
lissandra8 = pygame.image.load("lissandra8.jpeg")
lissandra9 = pygame.image.load("lissandra9.jpeg")


sol = pygame.image.load("sol.png")
AESTRELA = pygame.image.load("NASCEUMAESTRELA.png")


coracao = pygame.image.load("coracao.png")


raio = pygame.image.load("raio.png")

asheposicaocorreta = [0,0,0,0]
asheP1 = x , y = 354, 105
asheP2 = x , y = 499, 103
asheP3 = x , y = 352, 253
asheP4 = x , y = 500, 251

tela = menu1

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
             screen.blit(ashe1, (231, 153))
             screen.blit(ashe2, (37, 527))
             screen.blit(ashe3, (361, 527))
             screen.blit(ashe4, (542, 527))
             pygame.display.update()
        elif(peca == 'ashe2'):
             updateScreen(ashePuzzle)
             screen.blit(ashe1, (231, 153))
             screen.blit(ashe2, (37, 527))
             screen.blit(ashe3, (361, 527))
             screen.blit(ashe4, (542, 527))
             pygame.display.update()
        elif(peca == 'ashe3'):
             updateScreen(ashePuzzle)
             screen.blit(ashe1, (231, 153))
             screen.blit(ashe2, (37, 527))
             screen.blit(ashe3, (361, 527))
             screen.blit(ashe4, (542, 527))
             pygame.display.update()
        elif(peca == 'ashe4'):
             updateScreen(ashePuzzle)
             screen.blit(ashe1, (231, 153))
             screen.blit(ashe2, (37, 527))
             screen.blit(ashe3, (361, 527))
             screen.blit(ashe4, (542, 527))
             pygame.display.update()
    #Segunda posicao do quebra-cabeca         
    if(pos == 2):
        if(peca == 'ashe2'):
             updateScreen(ashePuzzle)
             screen.blit(ashe1, (366, 155))
             screen.blit(ashe2, (37, 527))
             screen.blit(ashe3, (361, 527))
             screen.blit(ashe4, (542, 527))
             pygame.display.update()
        elif(peca == 'ashe3'):
             updateScreen(ashePuzzle)
             screen.blit(ashe1, (194, 527))
             screen.blit(ashe2, (37, 527))
             screen.blit(ashe3, (366, 155))
             screen.blit(ashe4, (542, 527))
             pygame.display.update()
        elif(peca == 'ashe4'):
             updateScreen(ashePuzzle)
             screen.blit(ashe1, (194, 527))
             screen.blit(ashe2, (37, 527))
             screen.blit(ashe3, (361, 527))
             screen.blit(ashe4, (366, 155))
             pygame.display.update()
        elif(peca == 'ashe1'):
             updateScreen(ashePuzzle)
             screen.blit(ashe1, (194, 527))
             screen.blit(ashe2, (366, 155))
             screen.blit(ashe3, (361, 527))
             screen.blit(ashe4, (542, 527))
             pygame.display.update()
    #Terceira posicao do quebra-cabeca         
    if(pos == 3):
        if(peca == 'ashe3'):
             updateScreen(teste1)
             screen.blit(AESTRELA, (232, 257))
             screen.blit(sol, (37, 527))
             screen.blit(coracao, (361, 527))
             screen.blit(raio, (542, 527))
             pygame.display.update()
        elif(peca == 'coracao'):
             updateScreen(teste1)
             screen.blit(AESTRELA, (194, 527))
             screen.blit(sol, (37, 527))
             screen.blit(coracao, (232, 257))
             screen.blit(raio, (542, 527))
             pygame.display.update()
        elif(peca == 'raio'):
             updateScreen(teste1)
             screen.blit(AESTRELA, (194, 527))
             screen.blit(sol, (37, 527))
             screen.blit(coracao, (361, 527))
             screen.blit(raio, (232, 257))
             pygame.display.update()
        elif(peca == 'sol'):
             updateScreen(teste1)
             screen.blit(AESTRELA, (194, 527))
             screen.blit(sol, (232, 257))
             screen.blit(coracao, (361, 527))
             screen.blit(raio, (542, 527))
             pygame.display.update()
    #Quarta posicao do quebra-cabeca
    if(pos == 4):
        if(peca == 'estrela'):
             updateScreen(teste1)
             screen.blit(AESTRELA, (367, 257))
             screen.blit(sol, (37, 527))
             screen.blit(coracao, (361, 527))
             screen.blit(raio, (542, 527))
             pygame.display.update()
        elif(peca == 'coracao'):
             updateScreen(teste1)
             screen.blit(AESTRELA, (194, 527))
             screen.blit(sol, (37, 527))
             screen.blit(coracao, (367, 257))
             screen.blit(raio, (542, 527))
             pygame.display.update()
        elif(peca == 'raio'):
             updateScreen(teste1)
             screen.blit(AESTRELA, (194, 527))
             screen.blit(sol, (37, 527))
             screen.blit(coracao, (361, 527))
             screen.blit(raio, (367, 257))
             pygame.display.update()
        elif(peca == 'sol'):
             updateScreen(teste1)
             screen.blit(AESTRELA, (194, 527))
             screen.blit(sol, (367, 257))
             screen.blit(coracao, (361, 527))
             screen.blit(raio, (542, 527))
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
                     peca = 'ashe1' 

                if(c1x > 834 and c1x < 1021 and c1y > 93 and c1y < 244 and segundoclique):
                     peca = 'ashe2' 
                   
                if(c1x > 675 and c1x < 821 and c1y > 215 and c1y < 357 and segundoclique):
                     peca = 'ashe3'
                   
                if(c1x > 846 and c1x < 1027 and c1y > 287 and c1y < 468 and segundoclique):
                     peca = 'ashe4'                 

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
                
          



