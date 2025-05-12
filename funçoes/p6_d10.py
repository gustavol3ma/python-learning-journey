
frase = input("Digite uma frase: ")
frase = frase.replace(',',' ').replace('.',' ').replace('!',' ').replace('?',' ').split()

tamanho = list(filter(lambda x: len(x) >= 5, frase))
print(tamanho)