
# clientes

clientes = {

}

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

clientes['fabio'] = fabio
clientes['jessica'] = jessica
print(clientes)
print()
print(clientes['jessica'])
print(clientes['jessica']['nome'])
