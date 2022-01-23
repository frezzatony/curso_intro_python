#classe

class Calculadora():    
  
  def soma(self, a,b):
    return a+b
  
  def subtracao(self, a,b):
    return a-b
  
  def multiplcacao(self, a,b):
    return a*b
  
  def divisao(self, a,b):
    return a/b
  

calculadora = Calculadora()

print('soma: {}'.format(calculadora.soma(4,2)))
print('subtração: {}'.format(calculadora.subtracao(4,2)))
print('multiplicação: {}'.format(calculadora.multiplcacao(4,2)))
print('divisão: {}'.format(calculadora.divisao(4,2)))
  