from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    
    # Tabla de combinaciones ganadoras
    tabla_ganadora = (("PIEDRA","TIJERAS"),("PAPEL","PIEDRA"),("TIJERAS","PAPEL"))
    
    player = player.upper()
    ai = ai.upper()

    if (player,ai) in tabla_ganadora:
        resultado = 'Ganaste!'
    elif player == ai:
        resultado = 'Empate!'
    else:
        resultado = 'Perdiste!'
    
    return resultado  

# Entry Point
def Game():
    
    # La AI elige
    ai = randint(0,2)
    
    # El jugador elige
    player = int(input("Selecciona (1) Piedra, (2) Papel, (3) Tijeras: "))

    # Depuramos la entrada del jugador
    while player != 1 and player != 2 and player != 3:
        print ("Opción no válida")
        player = int(input("Selecciona (1) Piedra, (2) Papel, (3) Tijeras: "))

    # Decrementamos la opción para que nos sirva como índice de la tabla
    player-=1

    # Informamos de la elección de la AI
    print("Yo he elegido: "+options[ai]+", así que... ")
    

    winner = quienGana(options[player], options[ai])

    print(winner)

Game()