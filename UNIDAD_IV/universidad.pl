%hechos
profe_educa(raul,estructuras_de_datos).
profe_educa(cristian,bases_de_datos).
profe_educa(cristian,programacion).
profe_educa(joel,ia).
profe_educa(joel,ml).
profe_educa(joel,poo).

estudia(diego,ia).
estudia(nicol,ia).
estudia(alvaro,ia).
estudia(cba,ia).
estudia(felipe,ia).
estudia(felipe,ml).

%regla
es_alumno(P,A) :- 
profe_educa(P,C),
estudia(A,C).