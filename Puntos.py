# Función para recibir la cantidad de partidos ganados, empatados y perdidos y devolver los puntos conseguidos en total.
def Puntos(resultados):
    # Devuelvo los puntos totales que sería el resultado de multiplicar 3 por la posición 0
    # de resultados que son las victorias y sumar la posición 2 que son los empates
    return 3 * resultados[0] + resultados[2]