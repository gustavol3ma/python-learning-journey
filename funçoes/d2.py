numero_us = int(input('Digite um número de 1 a 10: '))

if numero_us > 10 or numero_us < 1:
    print('Erro, informe um número entre 1 e 10')
else:
    def tabuada(n: int):
        print(f'A tabuada do número {n}:')
        for i in range(11):
            resultado = n * i
            print(f'{n} X {i} = {resultado}')

    tabuada(numero_us)
