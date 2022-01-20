#condicionais

a = int(input('Entre com o valor de A: '))
b = int(input('Entre com o valor de B: '))

resto_a = a % 2
resto_b = b % 2

if resto_a == 0 or resto_b == 0:
  print('Foi digitado um numero par')
else:
  print('nao foi digitado um numero par')
