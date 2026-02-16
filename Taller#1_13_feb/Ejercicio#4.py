def elegantemente_tarde(llegadas,nombre):

    if nombre not in lista_llegadas:
        return False
    
    posicion = lista_llegadas.index(nombre)
    total_invitados = len(lista_llegadas)
    mid = total_invitados // 2

    if posicion >= mid and posicion != total_invitados - 1:

        return print(f"{nombre} llegó elegantemente tarde.")
    
    else:
        return print(f"{nombre} no llegó elegantemente tarde.")
    


lista_llegadas = ['Adela', 'Fleda','Owen','May','Mona','Gilbert','Ford']

for i in range(len(lista_llegadas)):
    print(elegantemente_tarde(lista_llegadas, lista_llegadas[i]))
   
