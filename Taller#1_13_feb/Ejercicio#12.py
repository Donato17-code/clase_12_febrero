def numero_palabras(frase):
    palabras = frase.split()
    return len(palabras)

texto = numero_palabras(input("ingrese una frase:"))
print(texto)