def colococoes(concorrentes):
    while True:
        
        #simulacao de pontos
        for i in range (0,5):
            #definindo as colocacoes em cada GP
            
            if concorrentes[i].getPos() == 1:
                concorrentes[i].setPontos(concorrentes[i].getPontos() + 25)
                
            elif concorrentes[i].getPos() == 2:
                concorrentes[i].setPontos(concorrentes[i].getPontos() + 18)
                
            elif concorrentes[i].getPos() == 3:
                concorrentes[i].setPontos(concorrentes[i].getPontos() + 15)
                
            elif concorrentes[i].getPos() == 4:
                concorrentes[i].setPontos(concorrentes[i].getPontos() + 12)
                
            else:
                concorrentes[i].setPontos(concorrentes[i].getPontos() + 10)
            
        break
def organiza(concorrentes):
    for i in range (0,4):
        if concorrentes[i].getPontos() < concorrentes[i + 1].getPontos():
            aux = concorrentes[i]
            concorrentes[i] = concorrentes[i + 1]
            concorrentes[i + 1] = aux