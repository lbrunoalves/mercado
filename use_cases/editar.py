from use_cases.adicionar import adicionarProduto
from use_cases.buscar import buscarPorCodigo
from repositorio import banco

def editarProduto(codigo, nome, categoria, preco):
    produto = buscarPorCodigo(codigo)
    if produto:
        produto['nome'] = nome
        produto['categoria'] = categoria
        produto['preco'] = preco
        print('Dados alterados com sucesso')
    else:
        print('Produto não encontrado!')

