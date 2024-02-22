import csv
fichero = open("liga.csv")
contenido = csv.reader(fichero)
def imprimirClasificacion(liga):
	#Recibe los datos de las demas funciones#
	datos=InfoEquipos(liga,*Equipos(liga))
	contador=1
	line = '-' * 61
	print(line)
	print("|   Nº    |     Equipo      |   PartidosGanados   |   PartidosPerdidos  |  PartidosEmpatados   |Puntos |")
	print(line)
	for dato in Clasificacion(datos):
		print('| {0:^6} | {1:^15} | {2:^6} |{3:^6} |{4:^6} |{5:^6} |'.format(contador,dato[0],dato[1],dato[2],dato[3],dato[4]))
		contador+=1
	print(line)