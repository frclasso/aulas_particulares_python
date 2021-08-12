
def novo_registro_usuario():
    """
    Cria as seguintes entradas de dados de clientes
    nome, sobrenome, email, telefone, empresa
    """ 
    nome = input('Digite seu nome:')
    sobrenome = input('Digite sobrenome: ')
    empresa = input("Digite nome da empresa: ")
    email = nome + "." + sobrenome + "@" + empresa + ".com.br" 

    usuario = []
    usuario.append(nome)
    usuario.append(sobrenome)
    usuario.append(empresa)
    usuario.append(email)

    return usuario

user1 = novo_registro_usuario()
user2 = novo_registro_usuario() # reaproveitando (segunda chamada da função)

# APPEND OU INSERT (CLIENTES)
clientes  = []
clientes.append(user1)
clientes.append(user2)
print(clientes)