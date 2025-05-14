aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]

#list Comprehension
#[expressão for elemento in coleção if condição]
lista = [tupla[1]  for tupla in  aluguel if tupla[0]=='Apartamento' ]
print(lista)