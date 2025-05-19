gabarito = ['D', 'A', 'B', 'C', 'A']

def corretor(testes: list):
    pontuacoes = []
    try:
        for teste in testes:
            nota = 0 
            for i in range(len(teste)):
                if teste[i] not in ['A', 'B', 'C', 'D']:
                    raise ValueError(f'A alternativa {teste[i]} não é uma opção de alternativa válida')
                elif teste[i] == gabarito[i]:
                    nota += 1 
            pontuacoes.append(nota) 
    except Exception as e:
        print(e)
    else:
        return pontuacoes

testes1 = [['D', 'A', 'B', 'C', 'A'], ['A', 'A', 'B', 'D', 'C'], ['D', 'E', 'B', 'C', 'A'] ,]
print(corretor(testes1))
