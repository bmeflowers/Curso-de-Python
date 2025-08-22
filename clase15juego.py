print("Juego de Piedra, Papel o Tijeras")
jugador1 = input("Jugador 1, ingresa tu nombre: ")
jugador2 = input("Jugador 2, ingresa tu nombre: ")

print("opciones posibles: piedra, papel o tijera")
moves = ["piedra", "papel", "tijera"]

eleccion1 = input(jugador1 + " Ingresa tu opcion: ")
eleccion2 = input(jugador2 + " Ingresa tu opción: ")

if eleccion1 not in moves or eleccion2 not in moves:
    print("Estas ingresando una opción inválida")
else:
    if eleccion1 == eleccion2 :
        print("empate")
    elif eleccion1 == "piedra" and eleccion2 == "tijera" or eleccion1 == "papel" and eleccion2 == "piedra" or eleccion1 == "tijera" and eleccion2 == "papel":
        print(jugador1 + "Gana!")
        print(jugador2 + "Perdiste")
    else:
        print(jugador2 + "Gana!")
        print(jugador1 + "Perdiste")

    




