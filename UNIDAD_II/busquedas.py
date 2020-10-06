from collections import deque
import sys, os
sys.setrecursionlimit(100000)



class nodo_estado:
    def __init__(self, EA, EP, A, n):
        self.valor = EA
        self.padre = EP
        self.accion = A
        self.nivel = n
        self.distancia = None

    def get_estado(self):
        return self.valor
    
    def get_padre(self):
        return self.padre

    def get_accion(self):
        return self.accion

    def get_nivel(self):
        return self.nivel

    def set_distancia(self, d):
        self.distancia = d
    
    def get_distancia(self):
        return self.distancia

    def __eq__(self, e):
        return self.valor == e


def ordenar_por_heuristica(e):
    return e.get_distancia()

class ocho_puzzle:
    estado_final = [nodo_estado("12345678H",None,"Final",None), nodo_estado("1238H4765",None,"Final",None)]
    def __init__(self, EI):
        self.estado_inicial = nodo_estado(EI, None, "Origen", 1)
        self.calcular_heuristica(self.estado_inicial)
        self.estado_actual = None
        self.historial = []
        self.cola_estados = deque()

    def add(self, ET):
        self.cola_estados.append(ET)
        self.historial.append(ET)

    def pop(self):
        return self.cola_estados.popleft()

    def esta_en_historial(self, e):
        return e in self.historial

    def es_final(self):
        return self.estado_actual in self.estado_final

    def mostrar_estado_actual(self):
        print("Estado Actual (H = " + str(self.estado_actual.get_distancia()) + ") [" + str(self.estado_actual.get_nivel()) + "] es:\n" + self.estado_actual.get_estado()[:3] + "\n" + self.estado_actual.get_estado()[3:6] + "\n" + self.estado_actual.get_estado()[6:] + "\n")

    def mostrar_estado(self, e):
        print("Estado  (H = " + str(e.get_distancia()) + ")  es:\n" + e.get_estado()[:3] + "\n" + e.get_estado()[3:6] + "\n" + e.get_estado()[6:] + "\n")

    def buscar_padre(self, e):
        if e.get_padre() == None:
            print("\n" + e.get_accion() + "\n Nivel: 1")
            self.mostrar_estado(e)
        else:
            self.buscar_padre(e.get_padre())
            print("\n" + e.get_accion() + "\n Nivel: " + str(e.get_nivel()))
            self.mostrar_estado(e)

    def mover(self, direccion):
        index = self.estado_actual.get_estado().find("H")

        if direccion == "UP":
            if index < 3:
                return "illegal"
            else:
                aux = self.estado_actual.get_estado()[index-3]

        """
        123
        4H6
        758

        aux = "2"
        """
        
        if direccion == "DOWN":
            if index > 5:
                return "illegal"
            else:
                aux = self.estado_actual.get_estado()[index+3]
        
        """
        123
        4H6
        758

        aux = "5"
        """

        if direccion == "LEFT":
            if index in [0,3,6]:
                return "illegal"
            else:
                aux = self.estado_actual.get_estado()[index-1]
        
        if direccion == "RIGHT":
            if index in [2,5,8]:
                return "illegal"
            else:
                aux = self.estado_actual.get_estado()[index+1]
        
        nuevo_estado = self.estado_actual.get_estado().replace("H","#")
        nuevo_estado = nuevo_estado.replace(aux,"H")
        nuevo_estado = nuevo_estado.replace("#", aux)
        return nuevo_estado

    def algoritmo_anchura(self, EI):
        iteracion = 1
        self.estado_actual = EI
        movimientos = ["UP","DOWN","LEFT","RIGHT"]

        while(not self.es_final()):
            print("Iteracion: " + str(iteracion) + "\n")
            self.mostrar_estado_actual()

            for movimiento in movimientos:
                estado_temporal = nodo_estado(self.mover(movimiento), self.estado_actual, "Mover a " + movimiento, self.estado_actual.get_nivel() + 1)
                if not self.esta_en_historial(estado_temporal) and not estado_temporal.get_estado() == "illegal":
                    self.add(estado_temporal) # se incluye en historial y en la cola

            print("\nElementos en Historial: " + str(len(self.historial)))
            print("\nElementos en Cola Estados: " + str(len(self.cola_estados)))

            #Paso a siguiente iteracion
            self.estado_actual = self.pop()
            iteracion += 1
        
        print("Iteracion: " + str(iteracion) + "\n")
        self.mostrar_estado_actual()
        print("\n\n\nHa llegado a Solucion!!!")
        self.buscar_padre(self.estado_actual)
        print("\nALGORITMO EN ANCHURA:")
        print("\nElementos en Historial: " + str(len(self.historial)))
        print("\nElementos en Cola Estados: " + str(len(self.cola_estados)))
        print("\nCantidad de Iteraciones: " + str(iteracion))

    def add_profundidad(self, pila_sucesores):
        while pila_sucesores.__len__() > 0:
            e = pila_sucesores.pop()
            self.historial.append(e)
            self.cola_estados.appendleft(e)

    def algoritmo_profundidad(self, EI):
        iteracion = 1
        self.estado_actual = EI
        movimientos = ["UP", "DOWN", "LEFT", "RIGHT"]
        sucesores = deque()

        while not self.es_final():
            print("Iteracion: " + str(iteracion) + "\n")
            self.mostrar_estado_actual()

            for movimiento in movimientos:
                estado_temporal = nodo_estado(self.mover(movimiento), self.estado_actual, "Mover a " + movimiento, self.estado_actual.get_nivel() + 1)
                if not self.esta_en_historial(estado_temporal) and not estado_temporal.get_estado() == "illegal":
                    sucesores.append(estado_temporal)
            
            self.add_profundidad(sucesores) 

            print("\nElementos en Historial: " + str(len(self.historial)))
            print("\nElementos en Cola Estados: " + str(len(self.cola_estados)))

            #Paso a siguiente iteracion
            self.estado_actual = self.pop()
            iteracion += 1

        print("Iteracion: " + str(iteracion) + "\n")
        self.mostrar_estado_actual()
        print("\n\n\nHa llegado a Solucion!!!")
        self.buscar_padre(self.estado_actual)
        print("\nALGORITMO EN PROFUNDIDAD:")
        print("\nElementos en Historial: " + str(len(self.historial)))
        print("\nElementos en Cola Estados: " + str(len(self.cola_estados)))
        print("\nCantidad de Iteraciones: " + str(iteracion))


    def distancia_estados(self, estado_presente, estado_objetivo):
        """Comparando estados, contando los espacios desubicados"""
        d = 0
        for i in range(len(estado_presente.get_estado())):
            if not estado_presente.get_estado()[i] == estado_objetivo.get_estado()[i]:
                d += 1
        return d

    def calcular_heuristica(self, estado):
        primero = True
        for final in self.estado_final:
            if primero:
                distancia = self.distancia_estados(estado, final)
                primero = False
            else:
                nueva_distancia = self.distancia_estados(estado, final)
                if nueva_distancia < distancia:
                    distancia = nueva_distancia
        estado.set_distancia(distancia)


    def algoritmo_primero_mejor(self, EI):
        iteracion = 1
        self.estado_actual = EI
        movimientos = ["UP", "DOWN", "LEFT", "RIGHT"]
        sucesores = []

        while not self.es_final():
            print("Iteracion: " + str(iteracion) + "\n")
            self.mostrar_estado_actual()

            for movimiento in movimientos:
                estado_temporal = nodo_estado(self.mover(movimiento), self.estado_actual, "Mover a " + movimiento, self.estado_actual.get_nivel() + 1)
                if not self.esta_en_historial(estado_temporal) and not estado_temporal.get_estado() == "illegal":
                    self.calcular_heuristica(estado_temporal)
                    sucesores.append(estado_temporal)
            
            sucesores.sort(key=ordenar_por_heuristica)
            self.add_profundidad(sucesores)

            print("\nElementos en Historial: " + str(len(self.historial)))
            print("\nElementos en Cola Estados: " + str(len(self.cola_estados)))

            #Paso a siguiente iteracion
            self.estado_actual = self.pop()
            iteracion += 1

        print("Iteracion: " + str(iteracion) + "\n")
        self.mostrar_estado_actual()
        print("\n\n\nHa llegado a Solucion!!!")
        self.buscar_padre(self.estado_actual)
        print("\nALGORITMO EN PRIMERO EL MEJOR:")
        print("\nElementos en Historial: " + str(len(self.historial)))
        print("\nElementos en Cola Estados: " + str(len(self.cola_estados)))
        print("\nCantidad de Iteraciones: " + str(iteracion))

    def add_beam(self, sucesores, b):
        for estado in sucesores:
            if b > 0:
                self.add(estado)
                b -= 1
            else:
                self.historial.append(estado)

    def algoritmo_beam(self, EI):
        iteracion = 1
        b = 2 # variable de corte
        sucesores = []
        self.estado_actual = EI
        movimientos = ["UP","DOWN","LEFT","RIGHT"]

        while(not self.es_final()):
            print("Iteracion: " + str(iteracion) + "\n")
            self.mostrar_estado_actual()

            for movimiento in movimientos:
                estado_temporal = nodo_estado(self.mover(movimiento), self.estado_actual, "Mover a " + movimiento, self.estado_actual.get_nivel() + 1)
                if not self.esta_en_historial(estado_temporal) and not estado_temporal.get_estado() == "illegal":
                    self.calcular_heuristica(estado_temporal)
                    sucesores.append(estado_temporal) # se incluye en historial y en la cola

            sucesores.sort(key=ordenar_por_heuristica)
            self.add_beam(sucesores, b)
            sucesores.clear()

            print("\nElementos en Historial: " + str(len(self.historial)))
            print("\nElementos en Cola Estados: " + str(len(self.cola_estados)))

            #Paso a siguiente iteracion
            self.estado_actual = self.pop()
            iteracion += 1
        
        print("Iteracion: " + str(iteracion) + "\n")
        self.mostrar_estado_actual()
        print("\n\n\nHa llegado a Solucion!!!")
        self.buscar_padre(self.estado_actual)
        print("\nALGORITMO EN BEAM:")
        print("\nElementos en Historial: " + str(len(self.historial)))
        print("\nElementos en Cola Estados: " + str(len(self.cola_estados)))
        print("\nCantidad de Iteraciones: " + str(iteracion))


    def algoritmo_hill_climbing(self, EI):
        iteracion = 1
        termina_bien = True
        self.estado_actual = EI
        movimientos = ["UP", "DOWN", "LEFT", "RIGHT"]
        sucesores = []

        while not self.es_final():
            print("Iteracion: " + str(iteracion) + "\n")
            self.mostrar_estado_actual()

            for movimiento in movimientos:
                estado_temporal = nodo_estado(self.mover(movimiento), self.estado_actual, "Mover a " + movimiento, self.estado_actual.get_nivel() + 1)
                if not self.esta_en_historial(estado_temporal) and not estado_temporal.get_estado() == "illegal":
                    self.calcular_heuristica(estado_temporal)
                    sucesores.append(estado_temporal)
            
            sucesores.sort(key=ordenar_por_heuristica)
            self.add_profundidad(sucesores)

            print("\nElementos en Historial: " + str(len(self.historial)))
            print("\nElementos en Cola Estados: " + str(len(self.cola_estados)))

            #Paso a siguiente iteracion
            estado_anterior = self.estado_actual
            self.estado_actual = self.pop()

            if estado_anterior.get_distancia() < self.estado_actual.get_distancia():
                print("\n\n\nNO llega a Solucion!!!")
                print("\nALGORITMO EN HILL CLIMBING:")
                print("\nElementos en Historial: " + str(len(self.historial)))
                print("\nElementos en Cola Estados: " + str(len(self.cola_estados)))
                print("\nCantidad de Iteraciones: " + str(iteracion))
                termina_bien = False
                break

            iteracion += 1
        
        if termina_bien:
            print("Iteracion: " + str(iteracion) + "\n")
            self.mostrar_estado_actual()
            print("\n\n\nHa llegado a Solucion!!!")
            self.buscar_padre(self.estado_actual)
            print("\nALGORITMO EN HILL CLIMBING:")
            print("\nElementos en Historial: " + str(len(self.historial)))
            print("\nElementos en Cola Estados: " + str(len(self.cola_estados)))
            print("\nCantidad de Iteraciones: " + str(iteracion))
        else:
            print("Termina Mal... que penita :(")

    def busqueda(self):
        self.add(self.estado_inicial)
        #self.algoritmo_anchura(self.pop())
        #self.algoritmo_profundidad(self.pop())
        #self.algoritmo_primero_mejor(self.pop())
        #self.algoritmo_beam(self.pop())
        self.algoritmo_hill_climbing(self.pop())

#MAIN
if __name__ == "__main__":
    puzzle = ocho_puzzle("123H56478")
    #puzzle = ocho_puzzle("8231H4765")
    #puzzle = ocho_puzzle("3158726H4")
    #puzzle = ocho_puzzle("1832H4765")

    puzzle.busqueda()
    
            