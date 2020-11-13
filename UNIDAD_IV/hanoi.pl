%Caso base
mover_disco(1, ORIGEN, DESTINO, _):-
    write('Se mueve disco tope desde el porte '),
    write(ORIGEN),
    write(' al poste '),
    write(DESTINO),
    nl.
%Caso recursivo
mover_disco(CANT_DISCOS, ORIGEN, DESTINO, CUALQUIERA) :-
    CANT_DISCOS > 1,
    NUEVA_CANT_DISCOS is CANT_DISCOS-1,
    mover_disco(NUEVA_CANT_DISCOS,ORIGEN,CUALQUIERA,DESTINO),
    mover_disco(1,ORIGEN,DESTINO,_),
    mover_disco(NUEVA_CANT_DISCOS,CUALQUIERA,DESTINO,ORIGEN).