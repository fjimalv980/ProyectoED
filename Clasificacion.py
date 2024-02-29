# Función que recibe la lista de infoEquipos y la ordena de mayor puntos a menor
def Clasificacion(datos_equipos):
    # Copio los datos de los equipos en otra variable para a la hora de hacer el sort, no modificar la lista original
    datos_orden=datos_equipos
    # Ordeno la lista por puntos. Con key cojo el quinto elemento de cada sublista y con reverse True que se ordene en descendente
    datos_orden.sort(key=lambda datos_equipos: datos_equipos[4],reverse=True)
    # Devuelvo la lista ordenada
    return datos_orden