

# lista

disciplinas = ['matematica', 'economia', 'fisica', 'estatistica']
print(type(disciplinas))
disciplinas.append('informatica')
disciplinas.insert(0, 'ciencia de dados')
print(disciplinas)
disciplinas.pop()
print(disciplinas)
print()
l1 = []
print(type(l1))

#tupla
outras = ('geografia', 'musica', 'artes')
print(type(outras))
# outras.append('quimica') # AttributeError: 'tuple' object has no attribute 'append'
# outras.pop() # AttributeError: 'tuple' object has no attribute 'pop'

#del(outras)
#print(outras)

t = (1,)
print(type(t))

outras = outras + ("historia",)
print(outras)

# tupla vazia
t2 = ()
print(type(t2))
print(outras[1:3])
print(outras[0])
print(outras[::-1])