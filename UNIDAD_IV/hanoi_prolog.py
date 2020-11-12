from pyswip import Prolog

prolog = Prolog()

prolog.consult("hanoi.pl")
solucion = prolog.query("mover_disco(3,izquierda,derecha,centro)")

for paso in solucion:
    print(paso)