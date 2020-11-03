from busqueda import busqueda

class jugador:

    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.es_bot = tipo
        self.cant_turnos = 0

    def set_simbolo(self, simbolo):
        self.simbolo = simbolo

    def toma_turno_automatico(self, matriz):
        if self.simbolo == "X":
            s_max = "X"
            s_min = "O"
        else:
            s_max = "O"
            s_min = "X"

        bot = busqueda(matriz, s_max, s_min)
        #bot = busqueda(matriz, "X", "O")
        nueva_matriz = bot.inicia_busqueda()
        return nueva_matriz
        
    def toma_turno_por_teclado(self, matriz):
        print("\n\nElige un espacio libre > Jugador: " + self.nombre)

        while True:
            while True:
                fila = int(input("Ingrese el numero de fila [0,2]: "))
                if fila >= 0 and fila <= 2:
                    break
            while True:
                columna = int(input("Ingrese el numero de columna [0,2]: "))
                if columna >= 0 and columna <= 2:
                    break
            if matriz[fila][columna] == " ":
                break

        matriz[fila][columna] = self.simbolo
        return matriz

    def toma_turno(self, matriz):
        self.cant_turnos += 1

        if self.es_bot:
            nueva_matriz = self.toma_turno_automatico(matriz)
        else:
            nueva_matriz = self.toma_turno_por_teclado(matriz)

        return nueva_matriz