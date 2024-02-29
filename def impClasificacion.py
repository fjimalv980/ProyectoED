def impClasificacion(liga):
    """
    Recibe la lista de diccionarios generada a partir del fichero CSV, genera los datos de la clasificación y los imprime por pantalla.
    """
    equipos = Equipos(liga)
    datos = InfoEquipos(liga, equipos)
    
    # Inicializar el contador para el número de equipos
    contador = 1
    
    # Línea para separar la cabecera y el contenido de la clasificación
    separador = '-' * 61
    
    # Imprimir el encabezado de la clasificación
    print(separador)
    print("|   №    |     Equipo      |   PG   |   PP  |  PE   |Puntos |")
    print(separador)
    
    # Iterar sobre los datos clasificados y mostrarlos en formato de tabla
    for equipo_info in Clasificacion(datos):
        # Formato de impresión para cada equipo
        print('| {0:^6} | {1:^15} | {2:^6} |{3:^6} |{4:^6} |{5:^6} |'.format(contador, equipo_info[0], equipo_info[1], equipo_info[2], equipo_info[3], equipo_info[4]))
        contador += 1
    
    # Imprimir la línea de separación al final de la clasificación
    print(separador)