"""
Para exercitar o que aprendemos em nossa primeira aula vamos definir algumas variáveis
e retornar os seus valores com o comando print.
"""

"""
Defina as seguintes variaveis, com seus respectivos valores:
nome, sobrenome, rua, bairro, cidade, cep, numero, telefone, email, empresa
1) crie dois registros diferentes e imprima as saídas; - ok
2) defina a vairavel nome completo reutilizando as variaves nome sobrenome (concatenar);
3) defina a variavel email_funcional concatenando (nome, sobrenome, @, empresa, .com.br)
"""

nome = "Fabio"
sobrenome = "Classo"
rua = "Salvatina Feliciana dos Santos"
bairro = "Itacorubi"
cidade = "Florianopolis"
cep = "88060-600"
numero = 263
telefone = "(48) 99174-3152"
email = ""
empresa= "rg contadores"

nome2 = "Juliana"
sobrenome2 = "Classo"
rua2 = "outro logradouro"
bairro2 = "Cachoeira do Bom Jesus"
cidade2 = "Florianopolis"
cep2 = "88060-000"
numero2 = 263
telefone2 = "(48) 99174-3152"
email2 = ""
empresa2 = "rg"


print("Dados do primeiro registro")
nome_completo = nome + " " +sobrenome
print(nome_completo)
print(f"Nome completo: {nome} {sobrenome}")
print(f"Nome completo: {nome_completo}")
email_funcional = nome.lower() + sobrenome.lower() + "@" + empresa.replace(" ", "") + ".com.br"
print(f"Endereço de email: {email_funcional}")