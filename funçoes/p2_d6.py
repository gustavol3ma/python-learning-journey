nota_do_aluno = []

for i in range(1,4):
    nota = float(input(f'Digite a {i} nota : '))
    nota_do_aluno.append(nota)

def situacao_do_aluno (notas):
    mai = max(nota_do_aluno)
    men = min(nota_do_aluno)
    media = sum(nota_do_aluno)/len(nota_do_aluno)
    if media > 6:
        sit = 'Aprovado'
    else:
        sit = 'Reprovado'
    return(media,mai,men,sit)

media , mai , men , sit = situacao_do_aluno(nota_do_aluno)

print(f"O(a) estudante obteve uma media de {media},\ncom a sua maior nota de {mai} pontos e a menor nota de {men} pontos e foi {sit}")