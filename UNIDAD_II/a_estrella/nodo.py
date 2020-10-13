import arco

class nodo:
    def __init__(self, x, y, nombre):
        self.x = x
        self.y = y
        self.nombre = nombre
        self.caminos = []

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    
    def get_nombre(self):
        return self.nombre

    def get_camino(self, indice):
        return self.caminos[indice]

    def get_caminos(self):
        return self.caminos

    def set_camino(self, nuevo_arco):
        self.caminos.append(nuevo_arco)

    def __eq__(self, n):
        if n == None:
            return False
        return self.x == n.get_x() and self.y == n.get_y()

    def __str__(self):
        """(A) = <-3,4>"""
        return "(" + self.nombre + ") = <" + str(self.x) + "," + str(self.y) + ">"