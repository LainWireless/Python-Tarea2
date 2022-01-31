edad = int(input("Introduzca su edad: "))
if edad < 0:
    print("La edad introducida se trata de un número negativo, ¿acaso usted ni siquiera ha sido gestado?")
elif edad >= 0 and edad <= 17:
    print("Usted es menor de edad.")
elif edad >=18:
    print("Usted es mayor de edad.")  