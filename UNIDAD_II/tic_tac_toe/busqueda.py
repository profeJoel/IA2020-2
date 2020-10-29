from estado import estado
from collections import deque
import sys, os
sys.setrecursionlimit(100000)

def ordenar_por_heuristica(e):
    return e.get_distancia()

class busqueda:
    
    def __init__(self, EI, s_max, s_min):
        self.estado_inicial = estado(EI, None, "Origen", 0)
        #self.calcular_heuristica(self.estado_inicial)
        self.estado_actual = None
        self.s_max = s_max
        self.s_min = s_min
        self.estado_solucion = None

    def calcular_p(self, s):
        m = self.estado_actual.get_estado()
        cant = 0
        for x in range(3):
            if m[x][0] in [s," "] and m[x][1] in [s," "] and m[x][2] in [s," "]:
                cant += 1
            if m[0][x] in [s," "] and m[1][x] in [s," "] and m[2][x] in [s," "]:
                cant += 1
        if m[0][0] in [s," "] and m[1][1] in [s," "] and m[2][2] in [s," "]:
            cant += 1
        if m[0][2] in [s," "] and m[1][1] in [s," "] and m[2][0] in [s," "]:
            cant += 1
        return cant

    def calcular_heuristica(self):
        return self.calcular_p(self.s_max) - self.calcular_p(self.s_min)
    
    def ver_espacios_libres(self):
        m = self.estado_actual.get_estado()
        h = []
        for i in range(3):
            for j in range(3):
                if m[i][j] == " ":
                    h.append([i,j])
        return h

    def juego_terminado(self):
        m = self.estado_actual.get_estado()
        for i in range(3):
            for j in range(3):
                if m[i][j] == " ":
                    return False
        return True

    def se_mueve_a(self, posicion, simbolo):
        nueva_matriz = self.estado_actual.get_estado()
        nueva_matriz[posicion[0]][posicion[1]] = simbolo
        return estado(nueva_matriz, self.estado_actual, " fila: " + str(posicion[0]) + " columna: " + str(posicion[1]), self.estado_actual.get_nivel() + 1)

    def mostrar_estado_actual(self):
        m = self.estado_actual.get_estado()
        print("\nTablero Actual:")
        for i in range(3):
            print(" " + m[i][0] + " | " + m[i][1] + " | " + m[i][2] + " ")
            if i < 2:
                print("___________")

    def algoritmo_minimax(self, e, p, t):
        self.estado_actual = e
        self.mostrar_estado_actual()

        if p == 0 or self.juego_terminado():
            self.estado_actual.set_heuristica(self.calcular_heuristica())
            return self.estado_actual.get_heuristica()
        elif t: #max
            hijos = []
            maximo = -10 # -infinito por definicion de la heuristica
            e_max = None
            posiciones_hijos = self.ver_espacios_libres()
            for posicion in posiciones_hijos:
                hijos.append(self.se_mueve_a(posicion,self.s_max))
            for hijo in hijos:
                eval = self.algoritmo_minimax(hijo, p - 1, False)
                if eval > maximo:
                    maximo = eval
                    e_max = hijo
            self.estado_solucion = e_max
            return maximo
        else: #min
            hijos = []
            minimo = 10 # -infinito por definicion de la heuristica
            e_min = None
            posiciones_hijos = self.ver_espacios_libres()
            for posicion in posiciones_hijos:
                hijos.append(self.se_mueve_a(posicion,self.s_min))
            for hijo in hijos:
                eval = self.algoritmo_minimax(hijo, p - 1, False)
                if eval < minimo:
                    minimo = eval
                    e_min = hijo
            self.estado_solucion = e_min
            return minimo
    
    def inicia_busqueda(self):
        self.algoritmo_minimax(self.estado_inicial, 2, True)
        return self.estado_solucion.get_estado()
