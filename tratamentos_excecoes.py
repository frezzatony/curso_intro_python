
lista = [1,10]

try:
  divisao = 10 / 1
  numero = lista[1]
  x=a
except ZeroDivisionError:
  print('Não é possível dividir por zero')
except IndexError:
  print('Erro ao acessar um índice inválido da lista')
except BaseException as exception:
  print('Erro não previsto: {}' .format(exception))
else:
  print('executa quando não ocorre nenhuma exceção')
finally:
  print('sempre executa, mesmo com falhas')