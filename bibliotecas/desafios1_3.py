'''
1. Escreva um código para instalar a versão 3.7.1 da biblioteca matplotlib.


python -m pip install --upgrade pip

Se estiver usando um ambiente virtual (recomendado), ative-o antes de rodar o comando.

pip install matplotlib==3.7.1
'''

'''
2. Escreva um código para importar a biblioteca numpy com o alias np.

import numpy as np 

'''

'''
3. Crie um programa que leia a seguinte lista de números e escolha um número desta aleatoriamente.

lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]

'''
from random import choice
lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
listaf = choice(lista)
print(f'O número escolhido foi {listaf}')