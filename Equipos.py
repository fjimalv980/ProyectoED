def Equipos(liga):
    """
    Función que recibe una lista de diccionarios con los datos de la liga y devuelve un conjunto con los equipos de la liga.

    Parámetros:
    - liga: Lista de diccionarios. Cada diccionario contiene información sobre un partido de la liga.

    Retorna:
    - Un conjunto con los nombres de los equipos que participan en la liga.
    """
    # Utilizamos una comprensión de lista para extraer el nombre del equipo1 de cada partido en la liga
    # y luego lo convertimos en un conjunto para eliminar duplicados
   
    equipos = set(partido.get("Team 1") for partido in liga if "Team 1" in partido)
    
    return equipos