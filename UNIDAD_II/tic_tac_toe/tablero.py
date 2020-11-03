from jugador import jugador

class tablero:

    def __init__(self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador1.set_simbolo("X")
        self.jugador2 = jugador2
        self.jugador2.set_simbolo("O")
        self.hay_ganador = False
        self.matriz = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def set_config(self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador1.set_simbolo("X")
        self.jugador2 = jugador2
        self.jugador2.set_simbolo("O")
        self.matriz = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def iniciar_matriz(self):
        self.matriz = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def insertar_movimiento(self, matriz):
        self.matriz = matriz
    
    def encuentra_tres_en_linea(self, s):
        m = self.matriz
        for x in range(3):
            if m[x][0] == s and m[x][1] == s and m[x][2] == s:
                return True
            if m[0][x] == s and m[1][x] == s and m[2][x] == s:
                return True
        if m[0][0] == s and m[1][1] == s and m[2][2] == s:
            return True
        if m[0][2] == s and m[1][1] == s and m[2][0] == s:
            return True

        return False

    def encuentra_ganador(self):
        return self.encuentra_tres_en_linea("X") or self.encuentra_tres_en_linea("O")
        
    def cant_espacios_libres(self):
        cant = 0
        for i in range(3):
            for j in range(3):
                if self.matriz[i][j] == " ":
                    cant += 1
        return cant

    def imprimir_matriz(self):
        print("\nTablero Actual:")
        for i in range(3):
            print(" " + self.matriz[i][0] + " | " + self.matriz[i][1] + " | " + self.matriz[i][2] + " ")
            if i < 2:
                print("___________")

    def inicia_partida(self):
        print("************INICIA PARTIDA************")
        self.iniciar_matriz()
        limite_turnos = 9
        i = 1

        while i <= limite_turnos:
            self.imprimir_matriz()
            
            if i%2 != 0:
                self.insertar_movimiento(self.jugador1.toma_turno(self.matriz))
            else:
                self.insertar_movimiento(self.jugador2.toma_turno(self.matriz))
            
            if self.encuentra_ganador():
                self.hay_ganador = True
                if i%2 != 0:
                    print("\nGanador:",self.jugador1.nombre,"con",str(self.jugador1.cant_turnos),"turnos")
                else:
                    print("\nGanador:",self.jugador2.nombre,"con",str(self.jugador1.cant_turnos),"turnos")
                break
            i += 1
        
        self.imprimir_matriz()
        if self.cant_espacios_libres() == 0 and not self.hay_ganador:
            print("\nEMPATE!!!")

        print("************FIN DE PARTIDA************")

                    

