# 1) inicializador/construtor - __init__
class Employee:

    # variavel global
    raise_ammount = 1.04  # 4%
    num_empregados = 0

    """Definicao de class"""
    def __init__(self, nome, sobrenome, company, salario): # atributos
        self.nome = nome
        self.sobrenome = sobrenome
        self.company = company
        self.salario = salario

        Employee.num_empregados += 1


    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    def email(self):
        return f'{self.nome.lower()}.{self.sobrenome.lower()}@{self.company.lower()}.com.br'

    def apply_raise(self): # localiza a instancia
        """Gera um aumento de 4%"""
        aumento = self.salario * self.raise_ammount
        return aumento

    @classmethod # localiza classe, modificar o comportamento da classe
    def set_raise_ammount(cls, amt):
        cls.raise_ammount = amt

    @classmethod
    def from_string(cls, data_str):
        nome, sobrenome, company, salario = data_str.split('-')
        return cls( nome, sobrenome, company, salario)


# intanciar a classe, criar um objeto
fabio = Employee('Fabio', 'Classo', 'FIESC', 50000)
luiza = Employee('Luiza', 'Camilo', 'FIESC', 60000)
print(fabio.nome)
print(fabio.sobrenome)
print(fabio.company)
print(fabio.email())
Employee.set_raise_ammount(1.05) # amt = 1.05
print(fabio.apply_raise())


print()
print(luiza.nome)
print(luiza.sobrenome)
print(luiza.company)
print(luiza.nome_completo())
print(f'Salario antes: {luiza.salario}')
#print(f'aumento: {luiza.salario * Employee.raise_ammount}')
print(luiza.apply_raise())


jones = Employee('Jones', 'None','Apple' ,5000 )

jane_str = 'Jane-Doe-Microsoft-30000'
j_nome, j_sobrenome, j_company,j_salario = jane_str.split('-')
jane = Employee(j_nome, j_sobrenome, j_company,j_salario)
print(jane.email())

print(f'Numero de colaboradores: {Employee.num_empregados}')

pedro_str = 'Pedro-Mariano-SomLivre-30000'
pedro = Employee.from_string(pedro_str)
print(pedro.email())