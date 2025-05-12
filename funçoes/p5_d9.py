dias = int(input("Quantas diárias? "))
cidade = input("Qual a cidade? [Salvador, Fortaleza, Natal ou Aracaju]: ").lower()
distancias = [850, 800, 300, 550]
passeio = [200, 400, 250, 300]
km_l = 14
gasolina = 5

def gasto_hotel(dias):
    return 150 * dias

def gasto_gasolina(cidade):
    if cidade == "salvador":
        return (2 * distancias[0] * gasolina) / km_l 
    elif cidade == "fortaleza":
        return (2 * distancias[1] * gasolina) / km_l 
    elif cidade == "natal":
        return (2 * distancias[2] * gasolina) / km_l 
    elif cidade == "aracaju":
        return (2 * distancias[3] * gasolina) / km_l 

def gasto_passeio(cidade, dias):
    if cidade=="salvador":
        return passeio[0] * dias
    elif cidade=="fortaleza":
        return passeio[1] * dias
    elif cidade=="natal":
        return passeio[2] * dias 
    elif cidade=="aracaju":
        return passeio[3] * dias 

gastos = gasto_hotel(dias) + gasto_gasolina(cidade) + gasto_passeio(cidade, dias)
print(f"Com base nos gastos definidos, uma viagem de {dias} dias para {cidade} saindo de Recife custaria {round(gastos, 2)} reais")