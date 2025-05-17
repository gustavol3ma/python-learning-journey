def converte_lista(lista):
    try:
        nova_lista = [float(elemento) for elemento in lista]
    except Exception as e:
        print(type(e), f'Erro: {e}')
        return []
    else:
        return nova_lista
    finally:
        print('Fim da execução da função')
