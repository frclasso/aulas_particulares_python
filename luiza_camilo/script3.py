

lista_de_clientes = [
      ['Parker', 'Peter', 44,'M','045045045', '454545-0',99998888,'MasterCard', 12345-0, '10/19', 215],
      ['Wayne', 'Bruce', 28,'F','345665045', '454545-0',99998888,'VISA', 12345-0, '10/19', 215],
      ['Jackson', 'Michael', 39,'M','045045045', '454545-0',99998888,'Nubank', 12345-0, '10/19', 215],
      ['Shorter', 'Wayne', 37,'M','045045045', '454545-0',99998888,'PayPal', 12345-0, '10/19', 215],
      ['Trump', 'Donald', 46,'M','045045045', '454545-0',99998888,'Credicard', 12345-0, '10/19', 215],
      ['Schuwazenerger', 'Arnold', 42,'M','045045045', '454545-0',99998888,'Elo', 12345-0, '10/19', 215],
      ['Marley', 'Bob', 40,'F','045045045', '454545-0',99998888,'American Express', 12345-0, '10/19', 215],
      ['Martino', 'Pat', 74,'M','045045045', '454545-0',99998888,'Dinners Club', 12345-0, '10/19', 215]
]


# ANALISE PREVIA DA ESTRUTURA DE DADOS
print(type(lista_de_clientes))

# VERIFICAR UM REGISTRO
print(lista_de_clientes[0]) # primeiro registro
print(type(lista_de_clientes[0])) 
print(lista_de_clientes[0][0]) # Parker, primeiro elemento da primeira lista
print()

# LOOP
for cliente in lista_de_clientes:
    #print(cliente)
    print(f"Sobrenome: {cliente[0]}, Nome: {[cliente[1]]}, Idade: {[cliente[2]]}")

print()
print()


def dados_do_cliente(linha):
    """Retorna dados de uma cliente"""
    _data = []
    for dados in linha:
        #print(dados)
        # tratamento ou não
        _data.append(dados) # adiciona dados do cliente a lista
    return _data

#print(dados_do_cliente(linha=lista_de_clientes[0]))

# SALVAR NUM ARQUIVO
# open /close()
# with open

def salva_registro(registro):
    with open("dados_clientes.txt", "a") as file: # w (Write), a (append), r (read)
        dados = registro 
        for dado in dados:
            #print(dado)
            file.write(str(dado))
            file.write(",")
        file.write("\n") # enter
        print("Dados salvos com sucesso")

salva_registro(dados_do_cliente(lista_de_clientes[1]))