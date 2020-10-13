from nodo import nodo
from arco import arco
from grafo import grafo

import math

class estado:
    def __init__(self, nodo, EP, A, n):
        self.valor = nodo
        self.padre = EP
        self.accion = A
        self.nivel = n
        self.g = -1
        self.h = -1


    def get_estado(self):
        return self.valor

    def get_padre(self):
        return self.padre

    def get_accion(self):
        return self.accion

    def get_nivel(self):
        return self.nivel
    
    def get_sucesores(self):
        return self.valor.get_caminos()

    def get_g(self):
        return self.g

    def get_h(self):
        return self.h

    def get_f(self):
        return (self.g + self.h)

    def set_g(self, e, coste):
        if e is None:
            self.g = -1
        else:
            #objetivo = e.get_estado()
            g_acumulado = e.get_g() if e.get_g() > 0 else 0
            #self.g = g_acumulado + math.sqrt((objetivo.get_y() - self.valor.get_y())**2 + (objetivo.get_x() - self.valor.get_x())**2)
            self.g = g_acumulado + coste

    def set_h(self, e):
        if e is None:
            self.h = -1
        else:
            objetivo = e.get_estado()
            self.h = math.sqrt((objetivo.get_y() - self.valor.get_y())**2 + (objetivo.get_x() - self.valor.get_x())**2)

    def __eq__(self, e):
        if e is None:
            return False
        return self.valor == e.get_estado() # comparando nodos del grafo

    def __str__(self):
        return "Estado Actual " + str(self.valor) + "\nAccion:\n" + self.accion + "\nNivel: " + str(self.nivel) + "\ng(e): " + str(self.g) + "\nh(e): " + str(self.h) + "\f(e): " + str(self.g + self.h) + "\n"