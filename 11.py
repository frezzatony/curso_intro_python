#listas e tuplas

lista = [1,3,5,7,]
lista_animal = ['cachorro','gato','elefante','abelha','lobo','arara']

print(lista)
print(type(lista))
print(lista_animal[1])

soma = 0
for x in lista:
  soma += x
print('soma: {}' .format(soma))

sumTotal = sum(lista)
print('sumTotal: {}' .format(sumTotal))
for x in lista_animal:
  print(x)

print('menor valor da lista_animal: {} ' .format(min(lista_animal)))

animalPesquisa = 'abelha'
print(animalPesquisa in lista_animal)

lista_animal.sort()
print(lista_animal)
lista_animal.extend(lista)
print(lista_animal)

#apresenta erro por serem tipos diferentes
#print(min(lista_animal))
