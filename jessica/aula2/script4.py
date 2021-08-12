# dicionarios

# vazio
d = {}
print(type(d))

fabio = {
    'nome': 'Fabio',
    'sobrenome':'Classo', 
    'logradouro':"Salvatina Feliciana dos Santos",
    'bairro':"Itacorubi",
    'cidade':"Florianopolis",
    'cep':"88060-600"
    }

print(type(fabio))
print(fabio)
print()


# dicionario ==> chaves(keys()) e valores(values())
# chaves ==> int ou str
# valores podem ser qq tipo Python(str, int, listas, tuplas, dicionarios)

#print(fabio.keys()) # retornar somente as chaves
#print(fabio.values())
#print(fabio.items())

# retornar valores
print(fabio['nome'])
print(fabio['sobrenome'])
print(fabio['logradouro'])
print(fabio['bairro'])
print(fabio['cidade'])
print(fabio['cep'])

# modificar
fabio['cep'] = '88040-600'
print(fabio)
print()

# adicionar
fabio['email'] = 'frclasso@yahoo.com.br'
print(fabio)
print()

# remover
fabio.pop('email')
print(fabio)
print()

fabio.__delitem__('cep')
print(fabio)
print()

fabio.popitem()  # removeu o ultimo item
print(fabio)
print()
