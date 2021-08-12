
# criar as seguintes entradas de dados de clientes
# nome, sobrenome, email, telefone, empresa

# -- APPEND OU INSERT (USUARIOS)
nome = input('Digite seu nome:')
sobrenome = input('Digite sobrenome: ')
empresa = input("Digite nome da empresa: ")
# email pode ser automatico
email = nome + "." + sobrenome + "@" + empresa + ".com.br" 
#print(email)

# saida
usuario = []
usuario.append(nome)
usuario.append(sobrenome)
usuario.append(empresa)
usuario.append(email)
#print(usuario)

# APPEND OU INSERT (CLIENTES)
clientes  = []
clientes.append(usuario)

############# SEGUNDO USUARIO
nome = input('Digite seu nome:')
sobrenome = input('Digite sobrenome: ')
empresa = input("Digite nome da empresa: ")
email = nome + "." + sobrenome + "@" + empresa + ".com.br" 

# saida
usuario = []
usuario.append(nome)
usuario.append(sobrenome)
usuario.append(empresa)
usuario.append(email)

# APPEND OU INSERT (CLIENTES)
clientes.append(usuario)
print(clientes)


