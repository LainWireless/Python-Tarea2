numero = float(input("Introduzca un número positivo: "))
if numero <= 0:
    print(("%.2f no es un número positivo. No es lo que se ha pedido.") %(numero))
else:
    if numero > 0:
        print(("%.2f es un número positivo.") %(numero))