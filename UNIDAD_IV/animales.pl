mas_grande(elefante,caballo).
mas_grande(caballo,burro).
mas_grande(burro,perro).
mas_grande(burro,mono).
mas_grande(mono,industrial).
mas_grande(perro,hormiga).

%reglas
/*es_mas_grande(X,Y) :- mas_grande(X,Y).
es_mas_grande(X,Y) :- mas_grande(X,Z),es_mas_grande(Z,Y).
*/
mas_grande(X,Y) :- mas_grande(X,Z), mas_grande(Z,Y).