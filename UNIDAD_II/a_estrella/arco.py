import nodo

class arco:
    def __init__(self, origen, destino, coste):
        self.origen = origen
        self.destino = destino
        self.coste = coste

    def get_origen(self):
        return self.origen

    def get_destino(self):
        return self.destino

    def get_coste(self):
        return self.coste

    def set_coste(self, coste):
        self.coste = coste

    def __eq__(self, a):
        if a == None:
            return False
        return self.origen == a.get_origen() and self.destino == a.get_destino()

    def __str__(self):
        return "|" + str(self.origen) + " -> " + str(self.destino) + "| = (" + str(self.coste) + ")"