from repositorio import banco
from use_cases.adicionar import adicionarProduto
from use_cases.buscar import buscarPorCodigo

def deletarProduto(codigo: int):
    produto = buscarPorCodigo(codigo)
    if produto:
        banco.remove(produto)
        print('Produto removido com sucesso!')
    else:
        print('Produto não encontrado!')


