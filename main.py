from interface import *
primeiro = projF("Max Verstappen",258)
segundo = projF("Charles Leclerc",178)
terceiro = projF("Sergio Perez",173)
quarto = projF("George Russel", 158)
quinto = projF("Carlos Sainz", 156)

#passando isso para uma vetor para que seja mais simples usar metodos
vetorPil = []
vetorPil.append(primeiro)
vetorPil.append(segundo)
vetorPil.append(terceiro)
vetorPil.append(quarto)
vetorPil.append(quinto)

tela = TelaAPP(vetorPil)
tela.inciar()