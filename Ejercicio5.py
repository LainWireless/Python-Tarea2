j1 = input ("Jugador 1 escoja, Piedra, Papel o Tijeras: ")
j2 = input ("Jugador 2 escoja, Piedra, Papel o Tijeras: ")

if j1 == "Piedra" and j2 == "Tijeras":
    print ("Jugador 1 gana.")
elif j1 == "Tijeras" and j2 == "Papel":
    print ("Jugador 1 gana.")
elif j1 == "Papel" and j2 == "Piedra":
    print ("Jugador 1 gana.")
elif j2 == "Piedra" and j1 == "Tijeras":
    print ("Jugador 2 gana.")
elif j2 == "Tijeras" and j1 == "Papel":
    print ("Jugador 2 gana.")
elif j2 == "Papel" and j1 == "Piedra":
    print ("Jugador 2 gana.")
else:
    if j1 and j2 == "Papel":
        print ("Empate.")
    elif j1 and j2 == "Piedra":
        print ("Empate.")
    elif j1 and j2 == "Tijeras":
        print ("Empate.")
    else:
        print ("Error.")