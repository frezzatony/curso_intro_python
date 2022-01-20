#lacos de repeticao
#numeros primos de 0 a 100

for i in range(0,101):
  divisao = 0;
  for x in range(1,i+1):
    resto = i % x
    if resto == 0:
      divisao += 1
  if divisao==2:
     print(x)

