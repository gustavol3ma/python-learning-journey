estados = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG']

#Armazenando os estados sem repetição de valor 
estados_unicos = list(set(estados))

#Criando uma lista de listas com valores repetidos de cada estado
lista_de_lista = []
for estado in estados_unicos:
    lista =[uf for uf in estados if uf == estado]
    lista_de_lista.append(lista)
print(lista_de_lista)

#criando um dicionário em que a chave é o nome de cada estado único e o valor é a contagem de elementos 

contagem_valores = {estados_unicos[i]: len(lista_de_lista[i])for i in range(len(estados_unicos))}

print(contagem_valores)