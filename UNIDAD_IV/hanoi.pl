mover_disco(1,ORIGEN,DESTINO,_) :-  
    write('Mueve disco tope desde poste '), 
    write(ORIGEN), 
    write(' al poste '), 
    write(DESTINO), 
    nl. 
mover_disco(CANT_DISCOS,ORIGEN,DESTINO,CUALQUIERA) :- 
    CANT_DISCOS > 1, 
    NUEVA_CANT_DISCOS is CANT_DISCOS-1, 
    mover_disco(NUEVA_CANT_DISCOS,ORIGEN,CUALQUIERA,DESTINO), 
    mover_disco(1,ORIGEN,DESTINO,_), 
    mover_disco(NUEVA_CANT_DISCOS,CUALQUIERA,DESTINO,ORIGEN).