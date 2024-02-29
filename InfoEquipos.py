#función que recibe la lista de diccionarios con los datos de la liga y el conjunto de equipos y devuelve 
#una lista de tuplas. En cada tupla se guarda un equipo con los partidos ganados, empatados,perdidos y los puntos.
#Esta función utiliza internamente:


import csv


def InfoEquipos(partidos,equipos):
	
    #iniciamos una lista vacia
	lista=[]
	
    #con un bucle for externo, recorremos la tupla que sale de Equipos()
	for equipo in equipos:
		#creamos una tupla para cada equipo y la iniciamos a 0 (ganados,empatados y perdidos).
		obtenido=[0,0,0]
		
        #usammos otro for para recorrer la lista de diccionarios con los datos de la liga, que sale de LeerPartidos()
		for partido in partidos:
			#vamos incrementando las valores si ganan, pierden o empatan
			#local:
			if partido["Team 1"]==equipo and QuienGana(partido["FT"])==0:
				obtenido[2]+=1 #empate
			elif partido["Team 1"]==equipo and QuienGana(partido["FT"])==-1:
				obtenido[1]+=1  #derrota
			elif partido["Team 1"]==equipo and QuienGana(partido["FT"])==1:
				obtenido[0]+=1  #victoria
			
			
				
            #visitante:
			if partido["Team 2"]==equipo and QuienGana(partido["FT"])==0:
				obtenido[2]+=1 #empate
			elif partido["Team 2"]==equipo and QuienGana(partido["FT"])==-1:
				obtenido[1]+=1  #derrota
			elif partido["Team 2"]==equipo and QuienGana(partido["FT"])==1:
				obtenido[0]+=1  #victoria
				
		#siguiendo dentro del for, voy añadiendo con append a la tupla de puntos el calculo de puntos y
		# le inserto en la primera posicion de la lista el nombre de cada equipo.
		obtenido.append(Puntos(lista))
		obtenido.insert(0,equipo)
			
        #meto cada tupla en la lista donde recogemos todos los resultados. 
		lista.append(tuple(lista))
	#devolvemos la lista final
	return lista