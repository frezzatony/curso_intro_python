a = 10
b = 5
soma = a + b
subtracao = a - b
multiplcacao = a * b
divisao = a/b
resto = a%b
print('soma: ' + str(soma))
print('subtracao:' + str(subtracao))
print('multiplcacao: ' + str(multiplcacao))
print('divisao: ' + str(divisao))
print('resto:' + str(resto))
#uma linha comentada

print('tipo de soma: ' + format(type(soma)))
print('tipo de divisao: ' + str(type(divisao)))

x = int('1')
soma2 = x + 1
print('x:' + str(x))

print('soma: {alias_soma}\n'
      'subtracao: {alias_subtracao}'.format(alias_soma=soma,alias_subtracao=subtracao))

print('um texto {alias_a}'.format(alias_a='primeiro alias sozinho')
