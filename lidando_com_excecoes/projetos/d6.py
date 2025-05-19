lista_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa', 'versátil',
                  'e', 'fácil', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos', 'desde',
                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial']
lista_nao_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa,', 'versátil',
                  'e', 'fácil,', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos,', 'desde',
                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial!']

def avalia_texto (texto: list ):
    for palavra in texto:
        if ',' in palavra or '.' in palavra or '!' in palavra or '?' in palavra:
            raise ValueError(f'O texto apresenta pontuações na palavra"{palavra}".')
    return "Texto já tratado!" 
    
    
# Testando no exemplo que não lança exceção
try:
  avaliacao = avalia_texto(lista_tratada)
except Exception as e:
  print(e)
else:
  print(avaliacao)

# Testando no exemplo que lança exceção

try:
  avaliacao = avalia_texto(lista_nao_tratada)
except Exception as e:
  print(e)
else:
  print(avaliacao)