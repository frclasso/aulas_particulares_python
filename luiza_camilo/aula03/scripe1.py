

id_clientes = [
      ('22112233', {'sobrenome':'Parker', 'nome':'Peter', 'idade':44,'sexo':'M', 'cpf':'045045045', 'telefone':9999888,
                    'cartaoCredito':'MasterCard', 'numeroCartao':'12345-0', 'dataValidade':'10/19',
                    'codigoSeguranca':215}),

      ('23112233', {'sobrenome':'Wayne','nome':'Bruce','idade':28,'sexo':'F','cpf':'345665045','telefone':99998888,
                     'cartaoCredito':'VISA', 'numeroCartao':'12345-0','dataValidade':'10/19','codigoSeguranca':215}),

      ('33221122', {'sobrenome':'Jackson','nome':'Michael','idade':39,'sexo':'M','cpf':'045045045','telefone':99998888,
                    'cartaoCredito':'Nubank','numeroCarato':'12345-0', 'dataVailidade':'10/19','codigoseguranca' :215}),

      ('44332211',{'sobrenome':'Shorter','nome':'Wayne','idade':37,'sexo':'M','cpf':'045045045','telefone':99998888,
                   'cartaoCredito':'PayPal','numeroCartao':'12345-0','dataValidade':'10/19','codigoSeguranca':215}),

      ('55443322',{'sobrenome':'Trump','nome':'Donald','idade':46,'sexo':'M','cpf':'045045045','telefone':99998888,
                   'cartaoCredito':'Credicard','numeroCartao':'12345-0','dataValidade':'10/19','codigoSeguranca':215}),

      ('66554433',{'sobrenome':'Schuwazenerger','nome':'Arnold','idade':42,'sexo':'M','cpf':'045045045','telefone':99998888,
                   'cartaoCredito':'Elo','numeroCartao':'12345-0', 'dataValidade':'10/19','codigoSeguranca' :215}),

      ( '77665566',{'sobrenome':'Marley','nome':'Bob','idade':40,'sexo':'F','cpf':'045045045','telefone':99998888,
                    'cartaoCredito':'American Express','numeroCartao':'12345-0', 'dataValidade':'10/19','codigoSeguranca':215}),

      ('88665577',{'sobrenome':'Martino','nome':'Pat','idade':74,'sexo':'M','cpf':'045045045','telefone':99998888,
                   'cartaoCredito':'Dinners Club', 'numeroCartao':'12345-0', 'dataValidade':'10/19','codigoSeguranca':215})

]
#print(type(id_clientes))
#print(id_clientes)

# verifando um registro
#print(type(id_clientes[0]))
#print(id_clientes[0])
print(id_clientes[0])
print(id_clientes[0][1])
print(type(id_clientes[0][1]))
print(id_clientes[0][1]['sobrenome'])

print()
for data in id_clientes[0]:
    print(data)

print()
for id, dados in id_clientes:
    #print(id, dados)
    print(id, dados['sobrenome'] ,dados['nome'], dados['cartaoCredito'])

print()

def dados_de_cliente(cliente):
    """Essa função extrai dados de um unico cliente"""

    # print(cliente[0])
    # print(cliente[1])

    # transformações  aqui...
    for data in cliente:
        #print(data)
        dados_clientes = []
        for k, v in cliente[1].items():
            #print(k, v)
            dados_clientes.append(v)
        return(dados_clientes)

print(dados_de_cliente(id_clientes[0]))

for indice, clients in enumerate(id_clientes):
    #print(indice)
    print(dados_de_cliente(id_clientes[indice]))
print()


# ENUMERATE
coisas = ['pedra', 'papel', 'tesoura']
for nr, coisa in enumerate(coisas):
    print(nr, coisa)
print()


# SALVAR OS REGISTRO FISICAMENTE

def salva_registro(cliente):
    print(dados_de_cliente(id_clientes[cliente]))
    with open('dados_clientes_novo.txt', 'a') as file_writer:
        for data in dados_de_cliente((id_clientes[cliente])):
            print(data)
            file_writer.write(str(data))
            file_writer.write(',')
        file_writer.write('\n')


#salva_registro(0)

for indice, clients in enumerate(id_clientes):
    #print(indice)
    print(salva_registro(indice))
print()