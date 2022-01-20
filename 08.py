#lacos de repeticao

numero = int(input('Entre com um número: '))
div=0

for x in range(1,numero+1):
  resto = numero % x
  print(numero,resto)
  
  if resto==0:
    div+=1

if div == 2:
  print('{} é primo'.format(numero))
else:
  print('{} NÃO é primo'.format(numero))

