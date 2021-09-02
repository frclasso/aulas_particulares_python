

# ler arquivo

#funcao open() [close()],  ou with open()

#open('instrumentos.csv')
#close()
import os

import csv

#print(os.getcwd())

caminho = "C:/Users/fabio.classo/Downloads/fabio/aulas_python/aulas_particulares_python/luiza_camilo/"

os.chdir(caminho)
#print(os.getcwd())


# 1) OBTIVE O ESTOQUE
def get_estoque():

    with open('instrumentos.csv', 'r') as file_reader:
        data = csv.reader(file_reader)
        #print(data)
        # for c in data:
        #     print(c)
        # print()
        keys, values = data
        #print(keys)
        #print(values)

        # juntar as duas listas em um dicionario
        estoque = dict(zip(keys, values)) # zip manipula listas
        #print(estoque)
        return estoque

#print(get_estoque())

# 2) RETORNEI O ESTOQUE POR PRODUTO
def verifica_qtd_instrumento_em_estoque(instrumento):
    estoque = get_estoque()
    if not instrumento in estoque:
        return

    for produto, quantidade in estoque.items():
        if produto == instrumento:
            #print(produto, quantidade)
            return quantidade

#print(verifica_qtd_instrumento_em_estoque('piano'))

# 4
# atualiza_estoque_base_de_dados
def atualiza_estoque_base_de_dados(estoque):
    """ REceber o estoque antigo, venda e atualizar(salvar fisicamente)"""
    # testar, criar um outro arquivo
    with open("instrumentos.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        #teste com dicionario qualquer
        #estoque = {"piano": 10, "saxfone":20 }
        writer.writerow(estoque.keys())
        writer.writerow(estoque.values())


#3 VENDA DO PRODUTO
def venda_de_instrumento(instrumento, venda):
    estoque = get_estoque()
    #print(verifica_qtd_instrumento_em_estoque(instrumento))
    value = int(estoque.get(instrumento))
    #print(type(value))
    
    #print(estoque)
    value -= venda
    #print(value)
    estoque[instrumento] = value
    #print(estoque)
    atualiza_estoque_base_de_dados(estoque)
    # atualizar estoque

#venda_de_instrumento('piano', 1)       
#atualiza_estoque_base_de_dados()

# 5 - INSERIR UM NOVO INSTRUMENTO NO CATALOGO
def insere_novo_produto_no_catalogo(produto, qtd=None):

    catalogo = get_estoque()
    print(catalogo)
    # update() dicionario anterior + {chave:valor}
    catalogo.update({produto:qtd})
    #print(catalogo)
    atualiza_estoque_base_de_dados(catalogo)

#insere_novo_produto_no_catalogo("teclado", 10)


# 6 - REMOVER UM PEODUTO DO CATALOGO 
def remove_produto_do_catalogo(produto):
    """Remove um item do catalogo"""
    catalogo = get_estoque()
    catalogo.__delitem__(produto) # __delitem__ (chave do dicionario)
    #print(catalogo)
    atualiza_estoque_base_de_dados(catalogo)

#remove_produto_do_catalogo("teclado")

from typing import Dict
# 7 - MULTIPLAS ENTRADAS
def estradas_no_estoque(entrada:Dict):

    estoque = get_estoque()
    print(entrada)
    estoque.update(entrada)
    print(estoque)
    atualiza_estoque_base_de_dados(estoque)
    
estradas_no_estoque({"teclaso":100, "xilofone": 56, "microfone":12})
