import sys, pygame
pygame.init()

size = width, height = 1020 , 550 

screen = pygame.display.set_mode(size)

menu1 = pygame.image.load("menu1.jpg")
instrucoes1 = pygame.image.load("instrucoes1.jpg")
opcoes1 = pygame.image.load("1.jpg")
creditos = pygame.image.load("creditos.jpg")
teste1 = pygame.image.load("NAOTEMNADA.png")

sol = pygame.image.load("sol.png")

AESTRELA = pygame.image.load("NASCEUMAESTRELA.png")


coracao = pygame.image.load("coracao.png")


raio = pygame.image.load("raio.png")

soposicaocorreta = [0,0,0,0]
estrelaposicaocorreta = x , y = 366, 155
coracaoposicaocorreta = x , y = 232, 257
raioposicaocorreta = x , y = 367, 257

tela = menu1

menuInicial = True
instrucoes = False
opcao = False
telaDeCreditos = False
jogar = False
tela1 = False


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
             updateScreen(teste1)
             screen.blit(sol, (231, 153))
             soposicaocorreta[0] = 1
             screen.blit(AESTRELA, (194, 527))
             screen.blit(coracao, (361, 527))
             screen.blit(raio, (542, 527))
             pygame.display.update()
    #Segunda posicao do quebra-cabeca         
    if(pos == 2):
        if(peca == 'estrela'):
             updateScreen(teste1)
             soposicaocorreta[1] = 1
    #Terceira posicao do quebra-cabeca         
    if(pos == 3):
        if(peca == 'coracao'):
             updateScreen(teste1)
             soposicaocorreta[2] = 1
        
    #Quarta posicao do quebra-cabeca
    if(pos == 4):
        if(peca == 'raio'):
             updateScreen(teste1)
             soposicaocorreta[3] = 1     
    if(soposicaocorreta[0] == 1):
       screen.blit(sol, (194, 527))
    else:
         

updateScreen(tela)
c1x = 0
c1y = 0
c2x = 0
c2y = 0
while 1:
    #Exibe posicao do mouse
    x, y = pygame.mouse.get_pos()
    #print('{} {} {} {} {} {} '.format(x,y,c1x, c1y, c2x, c2y))
    
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
               size = width, height = 759 , 688
               screen = pygame.display.set_mode(size)
               menuInicial = False
               jogar = True
               tela = teste1
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
                
            
