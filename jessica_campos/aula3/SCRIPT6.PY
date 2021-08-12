# OP ASSOSSIACAO

ids_funcioanarios = [122, 133, 144, 155, 166, 177, 188, 199, 200]

jessica = 122
fabio = 100
print(jessica in ids_funcioanarios) # true
print(fabio in ids_funcioanarios) # false
print(fabio not in ids_funcioanarios) # true

techs = ['Python', 'Django', 'Flask', 'Postgres']

print('Ruby' in techs)

# OP IDENTIDADE
# is
valor = 100
valor2 = 101

print(valor is valor2) # false
print(valor is 100) #true

# is not
print(valor is not valor2) # true
