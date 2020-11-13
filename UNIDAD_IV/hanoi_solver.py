from pyswip import Prolog

interprete = Prolog()

interprete.consult("hanoi.pl")
solucion = interprete.query("mover_disco(3,1,3,2)")

for paso in solucion:
    print(paso)