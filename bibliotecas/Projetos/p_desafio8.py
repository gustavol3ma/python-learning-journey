from random import choices

frutas = ["maçã", "banana", "uva", "pêra", 
          "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]

fruta_escolhida = choices(frutas,k=3)

print(f"A salada surpresa é: {fruta_escolhida[0]}, {fruta_escolhida[1]} e {fruta_escolhida[2]}")