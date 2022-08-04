from asyncio import events
from optparse import Values
import PySimpleGUI as sg
from pilotos import *
from campeaonato import *

class TelaAPP():
      def __init__(self,vetorPil: list) -> None:
            self.vetorPil = vetorPil
            
            self.tam = len(vetorPil)
            #layout
            layout = []
            for i in range (0,self.tam):

                layout += [sg.Text(vetorPil[i].getNome(), font='Fixedsys 20',size=(10,0),key=f'nome-{i}'),sg.Text('PTS',font='Fixedsys 20',justification='top',size=(3,0)),sg.Text(vetorPil[i].getPontos(),font='Fixedsys 20',size=(10,0),key=f'pontos-{i}' ),sg.Input(size=(5,5), font='Fixedsys 20', do_not_clear=False ,justification='right',key=f'pos-{i}')],
            layout += [[sg.Button('Calcular', font='Fixedsys 18', key='botao')]]

            self.window = sg.Window('Teste', layout,size=(470,500))
            
      def inciar(self) -> None:
          while (True):
                self.event, self.values = self.window.read()
                if self.event == 'Exit':
                    break
                else:
                    for j in range (0,self.tam):
                        self.vetorPil[j].setPos(int(self.values[f'pos-{j}']))
                    colococoes(self.vetorPil)
                    organiza(self.vetorPil)
                    for k in range(0,self.tam):
                        self.window[f'nome-{k}'].update(self.vetorPil[k].getNome())
                        self.window[f'pontos-{k}'].update(self.vetorPil[k].getPontos()) 
          self.window.close()          