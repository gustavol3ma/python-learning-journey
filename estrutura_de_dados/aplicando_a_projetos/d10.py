funcionarios = [('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6), ('SP', 10), ('MG', 4), ('ES',9), ('ES', 7), ('ES', 12), ('SP', 7), ('SP', 11), ('MG',8), ('ES',8), ('SP',9), ('RJ', 13), ('MG', 5), ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7), ('ES', 14), ('SP', 10), ('MG', 12)]

#Armazenando os estados sem repetição de valor
estados_unidos = list(set([tupla[0] for tupla in funcionarios]))
#print(estados_unidos)

#Criando uma lista de listas com valores de funcionários de cada estado 
lista_de_lista = []
for estado in estados_unidos:
    lista = [tupla[1] for tupla in funcionarios if tupla[0] == estado]
    lista_de_lista.append(lista)
print(lista_de_lista)

#Criando um dicionário com dados agrupados de funcionário por estado 
agrupamento_por_estado = {estados_unidos[i]:lista_de_lista[i] for i in range(len(estados_unidos))}

#Criando um dicionário com a soma de funcionários por estado
soma_po_estado = {estados_unidos[i]:sum(lista_de_lista[i]) for i in range(len(estados_unidos))}
print(soma_po_estado)