%hechos
gato(juanito).
gato(garfield).
gato(tom).
gato(copito_nieve).
gato(don_gato).
gato(felix).
gato(doraemon).
gato(silvestre).
gato(gato_con_botas).
gato(hello_kitty).

raton(mickey).
raton(jerry).
raton(mini).
raton(pinky).
raton(cerebro).
raton(speedy_gonzalez).
raton(stuart_little).
raton(remi).

enemigos(tom,jerry).

le_agrada(pinky,cerebro).

se_gustan(mickey,mini).
se_gustan(mini,mickey).

%reglas
cartoon(X,Y):- gato(X),raton(Y),enemigos(X,Y).

/*% :- se lee "si" o "implica que"
% , es un "&" o se puede leer "Conjunción"
% ; es un "|" o se puede leer "disjunción"

P :- Q;R.
P :- Q.
P :- R.

P :- Q,R;S,T,U.
P :- (Q,R);(S,T,U).
P :- Q,R.
P :- S,T,U.

% Aridad -> Arity -> Cardinalidad

% ejemplo
*/

amigos(X,Y) :- not(enemigos(X,Y)).
amigos(X,Y) :- le_agrada(X,Y); le_agrada(Y,X).
amigos(X,Y) :- pareja(X,Y); pareja(Y,X).

pareja(X,Y) :- se_gustan(X,Y), se_gustan(Y,X).
