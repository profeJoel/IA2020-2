from jugador import jugador
from tablero import tablero

#MAIN
if __name__ == "__main__":
    print("*********BIENVENIDOS AL GATO*********")
    nombre = input("Ingrese el nombre del Usuario: ")
    
    humano = jugador(nombre, False)
    
    nombre = input("Ingrese el nombre del Usuario: ")
    humano2 = jugador(nombre, False)
    #bot = jugador("BOT", True)

    #tictactoe = tablero(humano, bot)
    tictactoe = tablero(humano, humano2)
    tictactoe.inicia_partida()