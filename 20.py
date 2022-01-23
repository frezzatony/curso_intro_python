#modulos

from tv import Televisao

import os
tv = Televisao()
clear = lambda: os.system('cls') ;

while(not tv.power):
  clear()
  acao = input('Deseja ligar a tv?\n=>')
  if(str(acao).lower() ==  'sim'):
    tv.pressPoweButton()