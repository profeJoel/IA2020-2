from collections import deque
import time
import sys, os

sys.setrecursionlimit(100000)

def leer_mapa(mapa):
    archivo = mapa
    laberinto = []
    i = 0

    with open(archivo) as en_archivo:
        print("\n")
        for linea in en_archivo:
            laberinto.append([])
            posicion = linea.split(' ')
            for p in posicion:
                laberinto[i].append(p)
            i += 1
    
    return laberinto

class nodo_estado:
    def __init__(self, v, p, a, n):
        self.valor = v
        self.padre = p
        self.accion = a
        self.nivel = n

    def get_estado(self):
        return self.valor
    
    def get_padre(self):
        return self.padre

    def get_accion(self):
        return self.accion

    def get_nivel(self):
        return self.nivel
    
    def __eq__(self, e):
        return self.valor == e
    
class laberinto:
    estados_finales = [nodo_estado([3,4], None, "Final", None),nodo_estado([1,4], None, "Final", None)]

    def __init__(self, EI, mapa):
        self.estado_inicial = nodo_estado(EI, None, "Origen", 1)
        self.estado_actual = None
        self.historial = []
        self.cola_estados = deque()
        self.laberinto = mapa
        self.solucion = []

    def add(self, e):
        self.cola_estados.append(e)
        self.historial.append(e)

    def pop(self):
        return self.cola_estados.popleft()

    def esta_en_historial(self, e):
        return e in self.historial

    def es_final(self):
        return self.estado_actual in self.estados_finales

    def mostrar_estado_actual(self):
        os.system('cls')
        print("Estado Actual es: [" + str(self.estado_actual.get_estado()[0]) +","+ str(self.estado_actual.get_estado()[1]) + "]\n")
        x = self.estado_actual.get_estado()
        print(x)
        ce = self.cola_estados
        laberinto = self.laberinto
        texto = ""
        i = 0

        for fila in laberinto:
            texto = ""
            j = 0
            for lugar in fila:
                a = [i,j]
                if lugar == "1":
                    letra = "#"
                elif x[0] == i and x[1] == j:
                    letra = "O"
                elif a in self.estados_finales:
                    letra = "F"
                elif a in ce:
                    letra = "c"
                else:
                    letra = " "
                texto += letra
                j += 1
            print(texto)
            i += 1

    def mostrar_solucion(self, e):
        os.system('cls')
        x = self.estado_actual.get_estado()
        print(x)
        h = self.historial
        ce = self.cola_estados
        sol = self.solucion
        lab = self.laberinto
        texto = ""
        i = 0

        for fila in lab:
            texto = ""
            j = 0
            for lugar in fila:
                a = [i,j]
                if lugar == "1":
                    letra = "#"
                elif x[0] == i and x[1] == j:
                    letra = "O"
                elif a in self.estados_finales:
                    letra = "F"
                elif a in h:
                    if a in ce:
                        letra = "-"
                    elif a in sol:
                        letra = "*"
                    else:
                        letra = "h"
                else:
                    letra = " "
                
                texto += letra
                j += 1
            print(texto)
            i += 1


    def buscar_padres(self, e):
        if e.get_padre() == None:
            print("Listo")
        else:
            padre = e.get_padre()
            self.solucion.append(padre)
            self.buscar_padres(padre)

    def mover(self, direccion):

        laberinto = self.laberinto
        fila,columna = self.estado_actual.get_estado()
        nueva_coordenada = [3,3]

        if direccion == "N":
            if fila == 0:
                return "illegal"
            else:
                nueva_coordenada[0] = fila - 1
                nueva_coordenada[1] = columna

        if direccion == "S":
            if fila == len(laberinto) - 1:
                return "illegal"
            else:
                nueva_coordenada[0] = fila + 1
                nueva_coordenada[1] = columna
        
        if direccion == "O":
            if columna == 0:
                return "illegal"
            else:
                nueva_coordenada[0] = fila
                nueva_coordenada[1] = columna - 1

        if direccion == "E":
            if columna == len(laberinto[0]) - 1:
                return "illegal"
            else:
                nueva_coordenada[0] = fila
                nueva_coordenada[1] = columna + 1

        if laberinto[nueva_coordenada[0]][nueva_coordenada[1]] == "1":
            return "illegal"
        else:
            return nueva_coordenada
                
    
    def algoritmo_anchura(self, EI):
        iteracion = 1
        self.estado_actual = EI
        movimientos = ["N","S","O","E"]

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
            time.sleep(1)
        
        print("Iteracion: " + str(iteracion) + "\n")
        self.mostrar_estado_actual()
        print("\n\n\nHa llegado a Solucion!!!")
        self.buscar_padres(self.estado_actual)
        self.mostrar_solucion(self.estado_inicial)
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
        movimientos = ["N", "S", "O", "E"]
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
            time.sleep(1)

        print("Iteracion: " + str(iteracion) + "\n")
        self.mostrar_estado_actual()
        print("\n\n\nHa llegado a Solucion!!!")
        self.buscar_padres(self.estado_actual)
        self.mostrar_solucion(self.estado_inicial)
        print("\nALGORITMO EN PROFUNDIDAD:")
        print("\nElementos en Historial: " + str(len(self.historial)))
        print("\nElementos en Cola Estados: " + str(len(self.cola_estados)))
        print("\nCantidad de Iteraciones: " + str(iteracion))


    def busqueda(self):
        self.add(self.estado_inicial)
        #self.algoritmo_anchura(self.pop())
        self.algoritmo_profundidad(self.pop())



if __name__ == "__main__":
    coordenada = [0,0]
    lab = laberinto(coordenada, leer_mapa("laberinto_simple.dat"))
    lab.busqueda()