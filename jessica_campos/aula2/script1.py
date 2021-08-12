# listas

nome = "Fabio"
sobrenome = "Classo"
rua = "Salvatina Feliciana dos Santos"
bairro = "Itacorubi"
cidade = "Florianopolis"
cep = "88060-600"
numero = 263
telefone = "(48) 99174-3152"

clientes = ["Fabio", "Classo", "Salvatina Feliciana dos Santos", "Itacorubi", 
"Florianopolis", "88060-600", 263,"(48) 99174-3152" ]

# operações de lista

#indexar
#print(clientes[0])
#print(clientes[1])
#print(clientes[2])
#print(clientes[3])
nome = clientes[0]
sobrenome = clientes[1]
rua = clientes[2]
bairro = clientes[3]

# slice
#print(clientes[1:3])

print(clientes)
print(type(clientes))

print(nome)
print(sobrenome)
print(rua)
print(bairro)

# modificar - um unico valor
clientes[7] = "0800-777888" #sobrescreveu o valor
print(clientes)

# remover um item da lista
# pop
clientes.pop(7) # pop remove o ultimo elemento
print(clientes)

#remove
clientes.remove("Fabio") # passa o valor
print(clientes)

# delitem
clientes.__delitem__(5)  # passar o indice
print(clientes)

#del
del(clientes[0]) # passar indice, apagando um registro
print(clientes)
print()
del(clientes[:])# apagando todos os registros
print(clientes)
print()
#del(clientes) # apagando a lista
#print(clientes)


 # Adicionar elementos

# append - insere sempre no final da lista
novo_cliente = []
print(len(novo_cliente))
novo_cliente.append("Jessica")
novo_cliente.append("Campos")
novo_cliente.append("Rua do Sol")
novo_cliente.append("Vargem Pequena")
novo_cliente.append("Florianopolis")
novo_cliente.append("88060-800")
novo_cliente.append("(48)98989-1000")
print(novo_cliente)

# insert - insere onde vc definir
novo_cliente.insert(0, "10001")
print(novo_cliente)



