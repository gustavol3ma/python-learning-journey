notas = []

for i in range(1,6):
    nota = float(input(f'Digite nota {i}: '))
    notas.append(nota)

def media_do_sk(notas):
    notas.remove(max(notas))
    notas.remove(min(notas))
    return sum(notas)/len(notas)

resultado = media_do_sk(notas)
print(resultado)