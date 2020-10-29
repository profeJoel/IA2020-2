from collections import deque
import sys, os, math
from time import sleep

from nodo import nodo
from arco import arco
from grafo import grafo
from estado import estado

sys.setrecursionlimit(500000)

def ordenar_por_f(e):
    return e.get_f()

def ordenar_por_h(e):
    return e.get_h()

def ordenar_por_g(e):
    return e.get_g()

class busqueda:
    def __init__(self, nodo_inicial, nodo_final, archivo_grafo):
        self.tablero = grafo(archivo_grafo)
        self.estado_inicial = estado(self.tablero.buscar_nodo(nodo_inicial), None, "Inicial", 1)
        self.estado_final = estado(self.tablero.buscar_nodo(nodo_final), None, "Final", None)

        self.estado_inicial.set_g(self.estado_inicial,0)
        self.estado_inicial.set_h(self.estado_final)

        self.estado_actual = None
        self.historial = []
        self.cola_estados = deque()

    def add(self, e):
        self.cola_estados.append(e)
        self.historial.append(e)

    def pop(self):
        return self.cola_estados.popleft()

    def esta_en_historial(self, e):
        return e in self.historial
    
    def es_final(self):
        return self.estado_actual == self.estado_final

    def mover(self, sucesor):
        destino = sucesor.get_destino()
        nuevo_estado = estado(destino, self.estado_actual, "De " + self.estado_actual.get_estado().get_nombre() + " a " + destino.get_nombre(), self.estado_actual.get_nivel() + 1)
        nuevo_estado.set_g(self.estado_actual, sucesor.get_coste())
        return nuevo_estado

    def buscar_padres(self, e):
        if e.get_padre() == None:
            print(e)
        else:
            padre = e.get_padre()
            self.buscar_padres(padre)
            print(e)

    def traspasar_a_cola(self, lista, N):
        for e in lista:
            self.add(e)
        for n in range(0,N):
            self.cola_estados.appendleft(self.cola_estados.pop())

    def algoritmo_a_estrella(self, EI, i):
        self.estado_actual = EI
        cola_transitoria = []

        if self.es_final():
            self.buscar_padres(EI)
            print("ALGORITMO A* LLEGA A SOLUCION\nestado alcanzados: " + str(len(self.historial)) + "\nestados por explorar: " + str(len(self.cola_estados)) + "\niteraciones: " + str(i) + "\nCoste total Acumulado: " + str(self.estado_actual.get_f()))
        else:
            sucesores = self.estado_actual.get_sucesores()
            N = 0
            for sucesor in sucesores:
                estado_temporal = self.mover(sucesor)
                if not self.esta_en_historial(estado_temporal):
                    estado_temporal.set_h(self.estado_final)
                    cola_transitoria.append(estado_temporal)
                    N += 1
            cola_transitoria.sort(key=ordenar_por_f)
            #cola_transitoria.sort(key=ordenar_por_h)
            #cola_transitoria.sort(key=ordenar_por_g)
            self.traspasar_a_cola(cola_transitoria,N)

            return self.algoritmo_a_estrella(self.pop(), i + 1)

    def busqueda(self):
        self.add(self.estado_inicial)
        self.algoritmo_a_estrella(self.pop(),1)


#MAIN
if __name__ == "__main__":

    #experimento A -> D
    #origen = nodo(-3.0,4.0,"Origen")
    #destino = nodo(3.0,-2.0, "Destino")
    
    #experimento E -> D
    origen = nodo(-1.0,1.0,"Origen")
    destino = nodo(3.0,-2.0, "Destino")

    experimento = busqueda(origen, destino, "g1.txt")
    experimento.busqueda()


#####################
"""
a*          6   2   4   39
avara       4   1   3   49
uniforme    6   1   5   39
"""