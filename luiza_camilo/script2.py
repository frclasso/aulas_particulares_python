# keys/values

# CRIANDO DICIONARIOS VAZIOS

pessoas = {}# DICIONARIO VAZIO
print(type(pessoas))
print(pessoas)

pessoas_2 = {2,1,1,1,1,1,1,1,1,1,1,2,2, 1} # coleção unica de valores entre chaves, separados por virgulas
print(type(pessoas_2))
print(pessoas_2)
# set vazio
pessoas_3 = set()  
print(type(pessoas_3))

empregado = dict() # DICIONARIO VAZIO
print(type(empregado))

# CRIANDO UM DICIONARIO
users = {'id':1000, 'nome':'Fabio', 'cargo':'Eng Dados'}
print(type(users))
print(users)

# METODOS KEYS() VALUES() ITEMS()
print(users.keys())
print(users.values())
print(users.items())

for k, v in users.items():
    print(k, v)

print()

# ADICIONA ELEMENTOS EM UM DICIONARIO
fabio = {}
fabio['id'] = 1001
fabio['nome'] = 'Fabio'
fabio['sobrenome'] = 'Classo'
fabio['cargo'] = 'Dev'
fabio['natural'] = 'Rio de Janeiro'
fabio['nacionalidade'] = 'Brasil'
fabio['email'] = 'fabio@email.com'
fabio['time_futebol'] = 'flamengo'
#print(fabio)

# UPDATE
fabio['cargo'] = 'Developer'
print(fabio['cargo']) 
# ou
fabio.update({'cargo': 'Software Developer'})
print(fabio['cargo'])

fabio.update({'telefone': '08009001000'})

# REMOVER
# pop()
fabio.pop('time_futebol')

# del()
del(fabio['email'])
print(fabio)

# OBTER VALORES


# GET
print(fabio.get('funcao')) # None
#print(fabio['funcao'])

#for k, v in fabio.items():
#    print(k, v)

#APAGAR - clear()
fabio.clear()
print(fabio)

# apagar "o" dicionario
# del + nome do dicionario sem argumentos
#del fabio
#print(fabio) #NameError: name 'fabio' is not defined


# SET DEFAULT
user = {
    'id': 1,
    'nome': 'fabio',
    'cargo': 'developer'
    }

identificador = user.setdefault('id')
print(identificador)
email_corp = user.setdefault('email_corp')# se nao achar retorna None
print(email_corp)
telefone = user.setdefault('telefone','(48)08009002000')
print(telefone)
print(user)

# COPY
user_2 = user.copy()
print(id(user))
print(user_2)
print(id(user_2))

user_3 = user_2
print(id(user_3))