lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrado = lambda x : x**2

resultado = list(map(quadrado,lista))
print(resultado)