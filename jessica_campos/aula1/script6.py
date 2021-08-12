# STRINGS

frase = "Hello Python World"
print(frase)
print(type(frase))

# INDICES
print(frase[0])
print(frase[1])
print(frase[-1])

# SLICE/FATIAR
print(frase[0:5])  # n-1
print(frase[6:])
print(frase[6:12])  # limite inferior = 6, superior = 12
print()

variable1 = "Hello"
variable2 = "World"
frase2 = variable1 + " " + variable2 + "!"
print(frase2)
print()
print(id(frase2))  # pesquisar chamar pelo id
print(id(variable1))

# multiplicar *
print(variable1 * 5)
print("################################")
print("INICIO DO CALCULO DO IR")
print("#" * 32)
print()

lang = "Python"
print(lang[0])
print(lang[-6])
print(lang)
print(lang[:])
print(lang[::-1])