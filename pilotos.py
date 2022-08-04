class projF:
    def __init__(self, nome, pontos):
        self.nome = nome
        self.pontos = pontos
    def setPontos(self,pontos):
        self.pontos = pontos
    def setPos(self,pos: int)->None:
        self.pos = pos
    def getPos(self):
        return self.pos
    def getNome(self):
        return self.nome
    def getPontos(self):
        return self.pontos
    def imprimi(self):
        print("Piloto ", self.nome, " pontos = ", self.pontos,"\n")