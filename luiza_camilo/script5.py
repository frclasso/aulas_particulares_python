
dicionario_clientes = {
      '11223344':['Parker', 'Peter', 44,'M','045045045',99998888,'MasterCard', 12345-0, '10/19', 215],
      '22112233':['Wayne', 'Bruce', 28,'F','345665045',99998888,'VISA', 12345-0, '10/19', 215],
      '33221122':['Jackson', 'Michael', 39,'M','045045045',99998888,'Nubank', 12345-0, '10/19', 215],
      '44332211':['Shorter', 'Wayne', 37,'M','045045045',99998888,'PayPal', 12345-0, '10/19', 215],
      '55443322':['Trump', 'Donald', 46,'M','045045045',99998888,'Credicard', 12345-0, '10/19', 215],
      '66554433':['Schuwazenerger', 'Arnold', 42,'M','045045045',99998888,'Elo', 12345-0, '10/19', 215],
      '77665566':['Marley', 'Bob', 40,'F','045045045',99998888,'American Express', 12345-0, '10/19', 215],
      '88665577':['Martino', 'Pat', 74,'M','045045045',99998888,'Dinners Club', 12345-0, '10/19', 215]
}

# print(type(dicionario_clientes))
# for k , v in dicionario_clientes.items():
#     print(type(k), k, v)
# print()

#print(dicionario_clientes['11223344'])
print()

def dados_do_cliente(cliente):
    for k , v in dicionario_clientes.items():
        if k == cliente:
            #print(k,v)
            data = {k:v}
            #print(data)
            return data

#print(dados_do_cliente('11223344'))

# salvar
def salva_registro(registro):
    with open("dados_clientes_2.txt", "a") as file:
        dados = dados_do_cliente(registro)
        for k, v in dados.items():
            #print(k,v)
            file.write(k) # chave
            file.write(",")
            for data in v:
                #print(data)
                file.write(str(data))
                file.write(",")
        file.write("\n")
    print("dados salvos com sucesso")
salva_registro('11223344')