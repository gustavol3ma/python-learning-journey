
def divide_colunas(lista_1: list, lista_2: list) -> list:

  try:
    if len(lista_1) != len(lista_2): 
      raise ValueError("As listas precisam ter o mesmo tamanho")


    resultado = [round(a / b, 2) for a, b in zip(lista_1, lista_2)] 
  except ValueError as e:
    print(e)
  except ZeroDivisionError as e:
    print(f"{e}: A 2ª lista não pode possuir um valor igual a 0")
  else:
    return resultado
  
  # Testando no exemplo que não lança exceção
pressoes = [100, 120, 140, 160, 180]
temperaturas = [20, 25, 30, 35, 40]

divide_colunas(pressoes, temperaturas)

# Testando no exemplo que lança exceção (ZeroDivisionError)
pressoes = [60, 120, 140, 160, 180]
temperaturas = [0, 25, 30, 35, 40]

divide_colunas(pressoes, temperaturas)

# Testando no exemplo que lança exceção (ValueError)
pressoes = [100, 120, 140, 160]
temperaturas = [20, 25, 30, 35, 40]

divide_colunas(pressoes, temperaturas)