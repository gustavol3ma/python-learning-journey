idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}

try:
    chave = input('Informe o nome da pessoa : ')
    valor = idades[chave]
except KeyError:
    print('Nome não encontrado')
else:
    print(f'{chave} tem {valor} anos')