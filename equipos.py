import csv
def Equipos(liga):
	
	fichero = open("liga.csv")
	contenido = csv.reader(fichero)
	#Funcionn que recibe los datos de la liga y devuelve los equipos de la liga#
	return(tuple(set([partidos["equipo1"] for partidos in liga])))
