#conjuntos
#[] = lista
#() = tuplas
#{} = conjunto

conjuntoA = {1,2,3,4,5,}
conjuntoB = {5,6,7,8}

conjuntoUniao = conjuntoA.union(conjuntoB)
print(conjuntoUniao)

conjuntoInserceccao = conjuntoA.intersection(conjuntoB)
print(conjuntoInserceccao)

conjuntoDiferenca1 = conjuntoA.difference(conjuntoB)
conjuntoDiferenca2 = conjuntoB.difference(conjuntoA)
print('diferanca entre A e B: {} ' .format(conjuntoDiferenca1))
print('diferanca entre B e A: {} ' .format(conjuntoDiferenca2))

conjuntoDiffSimetrica = conjuntoA.symmetric_difference(conjuntoB)
print('diferança simétrica entre A e B: {} ' .format(conjuntoDiffSimetrica))

conjuntoC = {1,2,3}


conjuntoSubSet = conjuntoC.issubset(conjuntoA)
print('C é subconjunto de A: {}' .format(conjuntoSubSet))

conjuntoSuperSet = conjuntoA.issuperset(conjuntoC)
print('A é superconjunto de C: {}' . format(conjuntoSuperSet))