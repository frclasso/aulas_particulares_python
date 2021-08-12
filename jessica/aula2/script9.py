# frozenset()
numeros = {1,2,3,4,5,6,6,6,6,6,6,6,6,6,7,7,7,7,7,7,7}
print(type(numeros))
numeros.add(9)
print(numeros)

frozen_numeros = frozenset(numeros)
print(type(frozen_numeros))
print(frozen_numeros)
#frozen_numeros.add(120)
#print(frozen_numeros)