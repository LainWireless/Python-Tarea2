numero = int(input("Introduzca un número: "))
if numero % 4 == 0 and numero % 2 == 0:
    print ("El número es múltiplo de 4 y de 2.")
elif numero % 2 == 0:
    print ("El número es múltiplo de 2.")
else:
    if numero % 4 or numero % 2 != 0: 
        print ("No es múltiplo de 2.")