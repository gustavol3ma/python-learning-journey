
nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

nome_completo = map(lambda nome, sobrenome: f'{nome.title()} {sobrenome.title()}', nomes, sobrenomes)

for n in nome_completo:
  print(f'Nome completo: {n}')