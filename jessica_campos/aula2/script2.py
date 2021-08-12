

clientes = []

fabio = []

fabio.append("Fabio")
fabio.append("Classo")
fabio.append("Salvatina Feliciana dos Santos")
fabio.append("Itacorubi")
fabio.append("Florianopolis")
fabio.append("88060-600")
fabio.append(263)
fabio.append("(48) 99174-3152")

jessica = []
jessica.append("Jessica")
jessica.append("Campos")
jessica.append("Rua do Sol")
jessica.append("Vargem Pequena")
jessica.append("Florianopolis")
jessica.append("88060-800")
jessica.append("(48)98989-1000")

#print(fabio)
#print(jessica)

clientes.append(fabio)
clientes.append(jessica)
print(clientes)
print()
# retornando valores da primeira lista
print(clientes[0])
print()
print(clientes[1])

# inserir valores 
clientes[1].insert(6, 650)
print(clientes[1])

