#classe televisao
import os

class Televisao():
  def __init__(self):
    self.power = False
    self.canais = [1,2,3,4,5,6]
    self.volumesMinMax = [0,10]
    
    self.canalAtivo = 1
    self.volumeAtivo = 5
    self.clearTerminal = lambda: os.system('cls')  
  
  def pressPoweButton(self):
    self.power = False if self.power else True
    
    if self.power:
      self.menuTvLigada()

  def setCanal(self,canal):
    if canal not in self.canais:
      return False
    
    self.canalAtivo = canalAtivo
    return True
  
  def volumeUp(self):
    if self.volumeAtivo == max(self.volumesMinMax):
      return False
    
    self.volumeAtivo += 1
    return True
  
  def volumeDown(self):
    if self.volumeAtivo == min(self.volumesMinMax):
      return False
    
    self.volumeAtivo -= 1
    return True
  
  def menuTvLigada(self):
    self.clearTerminal()
    print('Bem vindo à sua TV!')
    
    menu = {
      1:  'Desligar a TV',
      2:  'Diminuir Canal',
      3:  'Aumentar Canal',
      4:  'Diminuir Volumne',
      5:  'Aumentar Volume'
    }
    
    
    while(self.power):
      
      for key,value in menu.items():
        print('[{}] {}'.format(key,value))
      
      acao = input('O que deseja: ')
      try: 
        acao = int(acao)
      except ValueError:
        acao = 0
     
      if not acao in menu:
        self.clearTerminal()
        continue
      
      self.clearTerminal()
      match acao:
        case 1:
            self.pressPoweButton()
      
      
      
    












