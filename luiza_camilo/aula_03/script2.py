

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


#3 VENDA DO PRODUTO

def venda_de_instrumento(instrumento, venda):
    estoque = get_estoque()
    #print(verifica_qtd_instrumento_em_estoque(instrumento))
    value = int(estoque.get(instrumento))
    #print(type(value))
    
    value -= venda
    print(value)

    # atualizar estoque


venda_de_instrumento('piano', 1)       


# funcao para atualizar estoque
# atualiza_estoque_base_de_dados




