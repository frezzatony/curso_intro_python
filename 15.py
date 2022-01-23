#listas e conuint
#conversoes entre tipos

lista = ['cachorro','gato','elefante','gato','cachorro']
print('tipo original de lista: {}' .format(type(lista)))
print('lista original: {}' .format(lista))

conjunto = set(lista)
print('tipo original de conjunto: {}' .format(type(conjunto)))
print('conjunto: {}' . format(conjunto))

lista = list(conjunto)
print('tipo conjunto para lista: {}' . format(type(lista)))
print('lista: {}' .format(lista))
