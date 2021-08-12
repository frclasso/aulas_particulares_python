

fabio = {
    'nome': 'Fabio',
    'sobrenome':'Classo', 
    'logradouro':"Salvatina Feliciana dos Santos",
    'bairro':"Itacorubi",
    'cidade':"Florianopolis",
    'cep':"88060-600"
    }


jessica = {
    'nome': 'Jessica', #
    'sobrenome':'Campos', 
    'logradouro':"Rua do Sol",
    'bairro':"Vargem Grande",
    'cidade':"Florianopolis",
    'cep':"88060-600"
    }

clientes = []
clientes.append(fabio)
clientes.append(jessica) # aqui

print(type(clientes))
print(type(clientes[1]))
print(clientes[1])
print()
clientes[1]['nome'] = 'Jéssica'
print(clientes[1])