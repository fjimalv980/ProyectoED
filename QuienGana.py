# Función que recibe un resultado y devuelve un número según este (1 victoria del local, 0 empate y -1 victoria del visitante)
def QuienGana(goles):
    # Guardo en una variable local, usando split para dividir en una lista, la posición [0] (equipo local) de un partido
    local=int(goles.split("-")[0])
    # Guardo en una variable visitante, usando split para dividir en una lista, la posición [1] (equipo visitante) de un partido
    visitante=int(goles.split("-")[1])
    # Si son iguales devuelvo 0 para empate
    if local==visitante:
        return 0
    # Si local es mayor a visitante, devuelvo 1 para victoria del local
    elif local>visitante:
        return 1
    # Si no, sólo queda visitante mayor a local y devuelvo 1 para victoria del visitante
    else:
        return -1