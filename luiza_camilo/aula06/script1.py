# classes

class Person:

    # inicializadores
    def __init__(self, name, role):
        self.name = name
        self.role = role

    # escopo global
    # atributos de classe
    empresa = "Wall Mart"
    __gratificacoes = 1000 # ENCAPSULAMENTO
    
    # escopo local
    def holerite(self):
        pass


fabio = Person("Fabio", "Programador")  # INTANCIANDO A CLASSE
print(fabio.name) # attr
print(fabio.role)


luiza = Person("Luiza", "Developer")# INTANCIANDO A CLASSE
print(luiza.empresa)
print(luiza.holerite())
print(luiza.__gratificacoes)