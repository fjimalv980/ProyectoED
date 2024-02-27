#función que lee el fichero y devuelve los datos en una lista de diccionarios.

import csv

def LeerPartidos():

	#guardamos en una variable la cabecera para no escribirla 8 veces
	cabecera= ["Date","Team 1","Team 2","FT","HT"]

	#iniciamos una lista vacia para los recoger los datos
	lista = []

	#usamos una excepcion por si no encontramos en fichero
	try:
		#abrimos el fichero y leemos su contenido con cvs reader
		fichero = open("liga.csv")
		contenido = csv.reader(fichero)

		#en un bucle for, leemos el contenido y lo vamos añadiendo a la lista
		for dato in contenido:
			#como queremos una lista de diccionarios, usamos la funcion zip para crearlo
			#cabecera contiene los nombres de las columnas y dato los valores correspondientes de una fila
			datos= dict(zip(cabecera,dato))
			#vamos añadiendo el diccionario a la lista
			lista.append(datos)
		fichero.close()

		#la funcion nos devuelve la lista
		return lista

		
	except FileNotFoundError:
		print("Fichero no encontrado")