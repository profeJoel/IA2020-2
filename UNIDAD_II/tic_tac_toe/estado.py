class estado:
    def __init__(self, EA, EP, A, n):
        self.valor = EA
        self.padre = EP
        self.accion = A
        self.nivel = n
        self.heuristica = None

    def get_estado(self):
        return self.valor
    
    def get_padre(self):
        return self.padre

    def get_accion(self):
        return self.accion

    def get_nivel(self):
        return self.nivel

    def set_heuristica(self, h):
        self.heuristica = h
    
    def get_heuristica(self):
        return self.heuristica

    def __eq__(self, e):
        return self.valor == e