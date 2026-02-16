def multiplos(numero):
    for numero in range(1,101):
        
        if numero % 3 == 0 and numero % 5 == 0:
            print(f"{numero} FizzBuzz")
        elif numero % 3 == 0:
            print (f"{numero} Fizz")
        elif numero % 5 == 0:
            print(f"{numero} Buzz")
        else:
            print(f"{numero} no es múltiplo de 3 ni de 5")

multiplos(100)