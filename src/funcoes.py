import math

def media_geometrica_lista(lista):
    if not isinstance(lista, list):
        return "Parâmetro deve ser lista"
    
    if len(lista) == 0:
        return "Lista tem que ter pelo menos um item"
    
    for item in lista:
        if not isinstance(item, (int, float)):
            return "Itens da lista devem ser números"

    resultado = 1
    
    for num in lista:
        resultado *= num
    
    resultado = math.pow(abs(resultado), 1/len(lista))
    
    return resultado