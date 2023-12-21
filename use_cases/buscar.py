from repositorio import banco

def buscarPorCodigo(codigo: int) -> dict or None:
    for produto in banco:
        if codigo == produto['codigo']:
            return produto
    return None

