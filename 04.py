#condicionais
a = int(input('Valor a: '))
b = int(input('Valor b: '))
c = int(input('Valor c: '))

if a>b:
  print('O maior é {A}'.format(A = a))
elif b>a and b>c:
    print('O maior é {B}'.format(B = b))
elif c>a and c>b:
    print('O maior é {C}'.format(C = c))
else:
  print('São iguais')

print('final do programa')






