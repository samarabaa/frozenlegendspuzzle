

import sys, pygame
pygame.init()

size = width, height = 1020 , 550 

screen = pygame.display.set_mode(size)

menu1 = pygame.image.load("menu1.jpg")
instrucoes1 = pygame.image.load("instrucoes1.jpg")
opcoes1 = pygame.image.load("1.jpg")
creditos = pygame.image.load("creditos.jpg")
niveis = pygame.image.load("niveis.jpeg")
teste1 = pygame.image.load("niveis.jpeg")
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


estrelaposicaocorreta = x , y = 366, 155
coracaoposicaocorreta = x , y = 232, 257
raioposicaocorreta = x , y = 367, 257

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

soposicaocorreta = [0,0,0,0]

segundoclique = False
primeiroclique = True
naoposicionou = True
peca = 'oi'
pos = 1

def updateScreen(menu1):
    screen.blit(menu1, (0, 0))
    if(solposicaocorreta):
        pygame.display.update()
    elif(estrelaposicaocorreta):
        pygame.display.update()
    elif(coracaoposicaocorreta):
        pygame.display.update()
    elif(raioposicaocorreta):
        pygame.display.update()
        
def movePeca(peca, pos):
    #Primeira posicao do quebra-cabeca
    if(pos == 1):
        if(peca == 'sol'):
             updateScreen(ashePuzzle)
             soposicaocorreta[0] = 1
             pygame.display.update()
    #Segunda posicao do quebra-cabeca         
    if(pos == 2):
        if(peca == 'estrela'):
             updateScreen(ashePuzzle)
             soposicaocorreta[1] = 1
    #Terceira posicao do quebra-cabeca         
    if(pos == 3):
        if(peca == 'coracao'):
             updateScreen(ashePuzzle)
             soposicaocorreta[2] = 1
        
    #Quarta posicao do quebra-cabeca
    if(pos == 4):
        if(peca == 'raio'):
             updateScreen(ashePuzzle)
             soposicaocorreta[3] = 1     
    if(soposicaocorreta[0] == 1):
       screen.blit(sol, (194, 527))
         

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
            if(jogar):
                if(naoposicionou):
                    screen.blit(AESTRELA, (194, 527))
                    screen.blit(sol, (37, 527))
                    screen.blit(coracao, (361, 527))
                    screen.blit(raio, (542, 527))
                    pygame.display.update()
                    naoposicionou = False
                                      
                #Define peca

                if(c1x > 194 and c1x < 294 and c1y > 526 and c1y < 620 and segundoclique):
                     peca = 'estrela' 
                if(c1x > 361 and c1x < 462 and c1y > 527 and c1y < 621 and segundoclique):
                     peca = 'coracao' 
                   
                if(c1x > 542 and c1x < 642 and c1y > 528 and c1y < 620 and segundoclique):
                     peca = 'raio'
                   
                if(c1x > 37 and c1x < 144 and c1y > 527 and c1y < 621 and segundoclique):
                     peca = 'sol'                 

                #Define posicao     
                if(c2x > 231 and c2x < 361 and c2y > 153 and c2y < 252 and primeiroclique):
                     pos = 1
                
                if(c2x > 366 and c2x < 507 and c2y > 155 and c2y < 252 and primeiroclique):
                     pos = 2
               
                if(c2x > 232 and c2x < 361 and c2y > 257 and c2y < 360 and primeiroclique):
                     pos = 3
             
                if(c2x > 367 and c2x < 508 and c2y > 257 and c2y < 359 and primeiroclique):
                     pos = 4
                print(peca)
                print(pos)
                print(c1x, c1y)
                print(c2x, c2y)
                if(primeiroclique):
                    movePeca(peca,pos)
                                          
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
                
            


