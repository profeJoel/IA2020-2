from estado import estado
from collections import deque
import sys, os, math
sys.setrecursionlimit(100000)

class busqueda:
    
    def __init__(self, EI, s_max, s_min):
        self.estado_inicial = estado(EI, None, "Origen", 0)
        self.s_max = s_max
        self.s_min = s_min
        self.estado_solucion = None
        self.estados_descubiertos = 0

    def calcular_p(self, e, s):
        #m = self.estado_actual.get_estado()
        m = e.get_estado()
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

    def se_interpone(self, e1, e2, e3, propio, rival):
        if (e1 == propio and e2 == rival and e3 == rival) or (e1 == rival and e2 == propio and e3 == rival) or(e1 == rival and e2 == rival and e3 == propio):
            return True
        return False

    def incluir_recompensa(self, e, propio, rival):
        m = e.get_estado()
        r = 0
        
        for x in range(3):
            if self.se_interpone(m[x][0], m[x][1], m[x][2], propio, rival):
                r += 10
                
            if self.se_interpone(m[0][x], m[1][x], m[2][x], propio, rival):
                r += 10

        if self.se_interpone(m[0][0], m[1][1], m[2][2], propio, rival):
            r += 10

        if self.se_interpone(m[0][2], m[1][1], m[2][0], propio, rival):
            r += 10

        return r
    def forzar_movimiento_ganador(self, e, propio):
        r = 0
        if self.encuentra_tres_en_linea(e, propio):
            r += 100
        return r

    def calcular_heuristica(self, e, t):
        if t:
            return self.calcular_p(e, self.s_max) - self.calcular_p(e, self.s_min) + self.incluir_recompensa(e, self.s_max, self.s_min) + self.forzar_movimiento_ganador(e, self.s_max)
        else:
            return self.calcular_p(e, self.s_min) - self.calcular_p(e, self.s_max) + self.incluir_recompensa(e, self.s_min, self.s_max) + self.forzar_movimiento_ganador(e, self.s_min)
        #return self.calcular_p(e, self.s_max) - self.calcular_p(e, self.s_min)
    
    def ver_espacios_libres(self, e):
        #m = self.estado_actual.get_estado()
        m = e.get_estado()
        h = []
        for i in range(3):
            for j in range(3):
                if m[i][j] == " ":
                    h.append([i,j])
        return h

    def encuentra_tres_en_linea(self, e, s):
        m = e.get_estado()
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

    def encuentra_ganador(self, e):
        return self.encuentra_tres_en_linea(e, "X") or self.encuentra_tres_en_linea(e, "O")
    
    """
    def juego_terminado(self, e):
        #m = self.estado_actual.get_estado()
        m = e.get_estado()
        for i in range(3):
            for j in range(3):
                if m[i][j] == " ":
                    return False
        return True
    """
    
    def juego_terminado(self, e):
        return len(self.ver_espacios_libres(e)) == 0 or self.encuentra_ganador(e)

    def se_mueve_a(self, e, posicion, simbolo):
        nueva_matriz = [row[:] for row in e.get_estado()]#copia el valor, no la referencia
        nueva_matriz[posicion[0]][posicion[1]] = simbolo
        
        return estado(nueva_matriz, e, " fila: " + str(posicion[0]) + " columna: " + str(posicion[1]), e.get_nivel() + 1)

    def mostrar_estado_actual(self, e):
        m = e.get_estado()
        print("\nTablero Actual:")
        for i in range(3):
            print(" " + m[i][0] + " | " + m[i][1] + " | " + m[i][2] + " ")
            if i < 2:
                print("___________")

    def algoritmo_minimax(self, e, p, t):
        if p == 0 or self.juego_terminado(e):
            e.set_heuristica(self.calcular_heuristica(e,t))
            self.estados_descubiertos += 1
            return e.get_heuristica()
        if t: #max
            hijos = []
            maximo = -math.inf # -infinito por definicion de la heuristica
            e_max = None
            posiciones_hijos = self.ver_espacios_libres(e)
            for posicion in posiciones_hijos:
                hijos.append(self.se_mueve_a(e, posicion, self.s_max))
            for hijo in hijos:
                #self.mostrar_estado_actual(hijo)
                eval = self.algoritmo_minimax(hijo, p - 1, False)
                #print("H(e)=",eval)
                if eval >= maximo:
                    maximo = eval
                    e_max = [row[:] for row in hijo.get_estado()]
            self.estado_solucion = [row[:] for row in e_max]
            #print(">>>>>Maximizando: ", maximo, "P:", p)
            #os.system("pause")
            return maximo
        else: #min
            hijos = []
            minimo = math.inf # +infinito por definicion de la heuristica
            e_min = None
            posiciones_hijos = self.ver_espacios_libres(e)
            for posicion in posiciones_hijos:
                hijos.append(self.se_mueve_a(e, posicion, self.s_min))
            for hijo in hijos:
                #self.mostrar_estado_actual(hijo)
                eval = self.algoritmo_minimax(hijo, p - 1, True) #arreglar para cambiar movimiento
                #print("H(e)=",eval)
                if eval <= minimo:
                    minimo = eval
                    e_min = [row[:] for row in hijo.get_estado()]
            self.estado_solucion = [row[:] for row in e_min]
            #print("<<Minimizando:", minimo, "P:", p)
            #os.system("pause")
            return minimo

    def algoritmo_minimax_alpha_beta(self, e, p, alpha, beta, t):
        if p == 0 or self.juego_terminado(e):
            e.set_heuristica(self.calcular_heuristica(e,t))
            self.estados_descubiertos += 1
            return e.get_heuristica()
        if t: #max
            hijos = []
            maximo = -math.inf # -infinito por definicion de la heuristica
            e_max = None
            posiciones_hijos = self.ver_espacios_libres(e)
            for posicion in posiciones_hijos:
                hijos.append(self.se_mueve_a(e, posicion, self.s_max))
            for hijo in hijos:
                #self.mostrar_estado_actual(hijo)
                eval = self.algoritmo_minimax_alpha_beta(hijo, p - 1, alpha, beta, False)
                #print("H(e)=",eval)
                if eval >= maximo:
                    maximo = eval
                    e_max = [row[:] for row in hijo.get_estado()]
                if eval >= alpha:
                    alpha = eval
                if beta <= alpha:
                    break
            self.estado_solucion = [row[:] for row in e_max]
            #print(">>>>>Maximizando: ", maximo, "P:", p)
            #os.system("pause")
            return maximo
        else: #min
            hijos = []
            minimo = math.inf # +infinito por definicion de la heuristica
            e_min = None
            posiciones_hijos = self.ver_espacios_libres(e)
            for posicion in posiciones_hijos:
                hijos.append(self.se_mueve_a(e, posicion, self.s_min))
            for hijo in hijos:
                #self.mostrar_estado_actual(hijo)
                eval = self.algoritmo_minimax_alpha_beta(hijo, p - 1, alpha, beta, True) #arreglar para cambiar movimiento
                #print("H(e)=",eval)
                if eval <= minimo:
                    minimo = eval
                    e_min = [row[:] for row in hijo.get_estado()]
                if eval >= beta:
                    beta = eval
                if beta <= alpha:
                    break
            self.estado_solucion = [row[:] for row in e_min]
            #print("<<Minimizando:", minimo, "P:", p)
            #os.system("pause")
            return minimo
    
    def inicia_busqueda(self):
        
        #print("\n\nResultado >>" + str(self.algoritmo_minimax(self.estado_inicial, 8, True)))
        print("\n\nResultado >>" + str(self.algoritmo_minimax_alpha_beta(self.estado_inicial, 8, -math.inf, math.inf, True)))
        
        print("Estados Descubiertos:", self.estados_descubiertos)

        #infinity = float('inf')

        
        return self.estado_solucion


        