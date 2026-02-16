def contar(texto):
    vocales = "aeiou"
    contador_vocales = 0
    contador_consonantes = 0
    texto=texto.lower()
    for letra in texto:
        if letra.isalpha():
            if letra in vocales:
                contador_vocales += 1
            else:
                contador_consonantes += 1
    return contador_vocales, contador_consonantes

resultado = contar(input("ingrese un texto:"))
print("vocales:", resultado[0])
print("consonantes:", resultado[1])