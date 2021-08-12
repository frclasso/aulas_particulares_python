data = [1, 'fabio', 'classo', 'frclasso@gmail.com']
print(type(data))
print()
data2 = tuple(data)
print(type(data2))

data3 = {}
data3['id'] = data[0]
data3['nome'] = data[1]
data3['sobrenome'] = data[2]
data3['email'] = data[3]
print(data3)
