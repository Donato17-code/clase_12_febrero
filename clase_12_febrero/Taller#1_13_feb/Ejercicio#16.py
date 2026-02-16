def anagramas(palabra1, palabra2):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()

    return sorted(palabra1) == sorted(palabra2)


if anagramas(input("ingrese la primera palabra:"), input("ingrese la segunda palabra:")):
    print("son anagramas")
else:
    print("no son anagramas")
    cout<<"no son anagramas"<<endl;