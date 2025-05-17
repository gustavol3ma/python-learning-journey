try:
    num1 = float(input('informe um número: '))
    num2 = float(input('Informe outro número: '))
    div = num1/num2
except Exception as e :
    print(type(e) , f'Erro{e}')
else:
    print(div)