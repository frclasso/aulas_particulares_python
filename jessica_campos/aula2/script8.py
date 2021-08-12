# dicionarios

# vazio
d = {}
print(type(d))

# sets
# vazio
numeros = set()  # casting - conversão de tipo
print(type(numeros))

# adição
numeros.add(10)
numeros.add(11)
numeros.add(12)
numeros.add(13)
numeros.add(14)
numeros.add(15)
numeros.add(15)
numeros.add(15)
numeros.add(15)
print(numeros)

# remover
numeros.pop()  #remove o primeiro, nao aceita args
print(numeros)

numeros.remove(15) # passar o valor exato como argumento
print(numeros)
numeros.add(15)
numeros.add(15)
numeros.add(15)
print(numeros)

num2 = {1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6}
print(num2)
frutas = {'banana','banana', 'banana','banana','pera'}
print(frutas)

# operacoes de conjunto
a = {1,2,3,4,5,6,7}
b = {6,7,8,9,10,11}
print(a & b) # interseção - {6, 7}
print(a ^ b) # XOR ou exclusivo
print(a - b) # somente os de 'a'
print(b - a) # somentes os de 'b'
print(a | b) # union
print(a and b) # 
print(b and a)
