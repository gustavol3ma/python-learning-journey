from random import randrange

nu_participantes = int(input("Digite o número de participantes: "))

if nu_participantes > 0:
    sorteado = randrange(nu_participantes)
    print(f"O número sorteado foi: {sorteado}")
else:
    print("Número de participantes inválido. Deve ser maior que 0.")