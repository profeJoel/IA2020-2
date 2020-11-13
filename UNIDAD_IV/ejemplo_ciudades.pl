temp_pmd_f(santiago, 70).
temp_pmd_f(arica, 80).
temp_pmd_f(punta_arenas, 30).
temp_pmd_f(puerto_montt, 50).

temp_pmd_c(CIUDAD, TEMP_C) :-
    temp_pmd_f(CIUDAD, TEMP_F),
    TEMP_C is (TEMP_F - 32) * 5 / 9.