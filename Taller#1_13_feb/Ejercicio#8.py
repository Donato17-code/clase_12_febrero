def elementos_comunes(lista1,lista2):
    comunes = []

    for elementos in lista1:
        if elementos in lista2:
            comunes.append(elementos)
    return comunes


lista1=[1,6,5,4,3,9]
lista2=[3,5,9,7,8,2]
print(elementos_comunes(lista1,lista2))