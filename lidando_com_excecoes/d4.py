def soma_lista(lista1,lista2):
    try:
        if len(lista1) == len(lista2):
            dados = [(lista1[i],lista2[i] , lista1[i]+lista2[i]) for i in range(len(lista1))]
        else:
            raise IndexError('A quantidade de elementos em cada lista é diferente.')
    except Exception as e:
        print(type(e),f'ERRO{e}')
    else:
        return dados