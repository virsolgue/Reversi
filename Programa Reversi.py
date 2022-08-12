DIMENSION_TABLERO=8
LETRAS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
FICHA_JUGADOR_1=("N")
FICHA_JUGADOR_2=("B")

def dar_bienvenida():
	"""Imprime por pantalla el nombre del juego."""
	print ("\n`OooOOo."                                     
			"\n o     `o                                 o"  
			"\n O      O                                  " 
			"\n o     .O                                  "  
			"\n OOooOO'  .oOo. `o   O .oOo. `OoOo. .oOo  O"  
			"\n o    o   OooO'  O   o OooO'  o     `Ooo. o"  
			"\n O     O  O      o  O  O      O         O O"  
			"\n O      o `OoO'  `o'   `OoO'  o     `OoO' o'") 
		
def preguntar_si_desea_comenzar_una_partida():
	"""Le solicita al usuario que ingrese por consola qué desea hacer: si desea comenzar a jugar (devuelve True en caso afirmativo (S), False en 
	caso negativo (N)), o bien muestra por pantalla las reglas del juego en el caso de que el usuario lo requiera (ayuda)."""
	while True:
		entrada=input("¿Desea comenzar una nueva partida? S / N "
					"\n¿Primera vez en Reversi? Ingrese A (Ayuda) para aprender a jugar.")		
		if entrada.upper()=="A":
			reglamentar_juego()
		if entrada.upper()=="S" or entrada.upper()=="N": 
			return entrada.upper()
		print("Opción inválida. Por favor, vuelva a ingresar una respuesta.") 	
	
def reglamentar_juego():
	"""Muestra por pantalla las reglas del juego Reversi."""
	print ("\nREGLAS DEL JUEGO"                                     
			"\n -----------------------------------------------------------------------------"  
			"\n El juego Othello, también conocido como Reversi, se desarrolla sobre un" 
			"\n tablero en el que inicialmente se sitúan dos fichas negras y dos fichas" 
			"\n blancas dispuestas en forma cruzada en el centro del tablero. Comienza el"  
			"\n primer jugador con las fichas negras, colocando una ficha en una posición"   
			"\n en la que, al colocarla, encierre una ficha del oponente en cualquier"   
			"\n dirección, por una ficha negra ya existente en el tablero y la ficha colocada." 
			"\n Se considerará ganador al jugador que más casillas del tablero haya ocupado" 
			"\n con su color. El juego finaliza a las 60 jugadas o cuando ningún jugador"
			"\n tenga jugadas posibles para realizar (lo que ocurra primero)."
			"\n -----------------------------------------------------------------------------")

def solicitar_nombres_jugadores():
	"""Se le solicitará a cada uno de los dos jugadores que ingresen su nombre por consola. Para el primer nombre ingresado devuelve la 
	variable nombre_jugador_1 y para el segundo, devolverá la variable nombre_jugador_2.""" 
	nombre_jugador_1=input("¡Bienvenido Jugador_1! Por favor, a continuación ingrese su nombre.")
	nombre_jugador_2=input("¡Bienvenido Jugador_2! Por favor, a continuación ingrese su nombre.")
	return nombre_jugador_1, nombre_jugador_2
	
def imprimir_tablero_inicial():
	"""Imprime por pantalla una representación gráfica del tablero. Separa los casos en los que la dimensión del tablero es par por un lado, y los 
	casos en los que es impar por otro."""
	separacion_filas= " +---+"+"---+"*(DIMENSION_TABLERO-2)+"---+"
	separacion_columnas= "|   |"+"   |"*(DIMENSION_TABLERO-2)+"   |"
	encabezado=" "
	for i in range (1,DIMENSION_TABLERO+1):
		if i<10:
			encabezado+="  "+str(i)+" "	
		else:
			encabezado+=" "+str(i)+" "
	print (encabezado)
	fila=0
	if DIMENSION_TABLERO%2==0: 
		for i in range (1,int(DIMENSION_TABLERO/2)):
			fila+=1
			print (separacion_filas)
			print (LETRAS[i-1]+separacion_columnas)
		print (separacion_filas)
		print (LETRAS[fila]+"|   |"+"   |"*(int(DIMENSION_TABLERO/2)-2)+" B |"+" N "+"|   "*(int(DIMENSION_TABLERO/2)-2)+"|   |")
		print (separacion_filas)
		print (LETRAS[fila+1]+"|   |"+"   |"*(int(DIMENSION_TABLERO/2)-2)+" N |"+" B "+"|   "*(int(DIMENSION_TABLERO/2)-2)+"|   |")
		fila+=1
		for i in range (1,int(DIMENSION_TABLERO/2)):
			fila+=1
			print (separacion_filas)
			print (LETRAS[fila]+separacion_columnas)
		print (separacion_filas)
	else:
		dimension_par_anterior=DIMENSION_TABLERO-1
		for i in range (1,int(dimension_par_anterior/2)):
			fila+=1
			print (separacion_filas)
			print (LETRAS[i-1]+separacion_columnas)
		print (separacion_filas)	
		print (LETRAS[fila]+"|   |"+"   |"*(int(dimension_par_anterior/2)-2)+" B |"+" N "+"|   "*(int(dimension_par_anterior/2)-1)+"|   |")
		print (separacion_filas)
		print (LETRAS[fila+1]+"|   |"+"   |"*(int(dimension_par_anterior/2)-2)+" N |"+" B "+"|   "*(int(dimension_par_anterior/2)-1)+"|   |")
		fila+=1
		for i in range (1,int(dimension_par_anterior/2)+1):
			fila+=1
			print (separacion_filas)
			print (LETRAS[fila]+separacion_columnas)
		print (separacion_filas)
		
def generar_tablero():
	"""Genera la lista de cadenas que representará el contenido de cada posición en el tablero. Dependerá de las dimensiones del mismo (DIMENSION_TABLERO).
	Estará formada por cadenas vacías y por las 4 fichas que ocupan el centro del tablero."""
	tablero=[]
	for filas in range (1,DIMENSION_TABLERO+1):
		for columnas in range (1,DIMENSION_TABLERO+1):
			tablero.append(" ")
	tablero.append(" ")
	
	#SE REEMPLAZAN LAS CUATRO FICHAS CENTRALES EXISTENTES AL COMIENZO DE LA PARTIDA
	if DIMENSION_TABLERO%2==0:
		tablero[(int(DIMENSION_TABLERO/2) -1)*DIMENSION_TABLERO+int(DIMENSION_TABLERO/2)]=FICHA_JUGADOR_2
		tablero[(int(DIMENSION_TABLERO/2) -1)*DIMENSION_TABLERO+int(DIMENSION_TABLERO/2)-1]=FICHA_JUGADOR_1
		tablero[int(DIMENSION_TABLERO/2)*DIMENSION_TABLERO+int(DIMENSION_TABLERO/2)]=FICHA_JUGADOR_1
		tablero[int(DIMENSION_TABLERO/2)*DIMENSION_TABLERO+int(DIMENSION_TABLERO/2)-1]=FICHA_JUGADOR_2	
	else:
		dimension_par_anterior=DIMENSION_TABLERO-1
		tablero[(int(dimension_par_anterior/2) -1)*DIMENSION_TABLERO+int(DIMENSION_TABLERO/2)]=FICHA_JUGADOR_2
		tablero[(int(dimension_par_anterior/2) -1)*DIMENSION_TABLERO+int(DIMENSION_TABLERO/2-1)]=FICHA_JUGADOR_1
		tablero[int(dimension_par_anterior/2)*DIMENSION_TABLERO+int(DIMENSION_TABLERO/2)]=FICHA_JUGADOR_1
		tablero[int(dimension_par_anterior/2)*DIMENSION_TABLERO+int(DIMENSION_TABLERO/2)-1]=FICHA_JUGADOR_2
	return tablero
				
def imprimir_tablero_en_juego(tablero):	
	"""Recibe la variable tablero (lista de cadenas), e imprime el tablero en pantalla con las fichas en juego."""
	separacion_filas= " +----+"+"----+"*(DIMENSION_TABLERO-2)+"----+"
	fila_tablero=[]
	encabezado=" "
	for i in range (1,DIMENSION_TABLERO+1):
		if i<10:
			encabezado+="   "+str(i)+" "	
		else:
			encabezado+="  "+str(i)+" "
	print (encabezado)
	print (separacion_filas)
	for fila in range (1,DIMENSION_TABLERO+1):
		contenido_fila="|"
		fila_tablero=tablero[DIMENSION_TABLERO*(fila-1):DIMENSION_TABLERO*fila]
		for element in range (0,DIMENSION_TABLERO):
			contenido_fila+="  "+fila_tablero[element]+" |"
		print (LETRAS[fila-1]+contenido_fila)
		print (separacion_filas)

def asignar_turno(numero_de_jugada):
	"""Mediante la distinción de número de jugadas por pares e impares, se devolverá Jugador_1 en el caso de que el numero de jugada sea impar (el Jugador_1
	es quien comienza a jugar), y en el caso de que la jugada sea par, se devuelve Jugador_2."""
	if numero_de_jugada%2==0:
		return (FICHA_JUGADOR_2)
	else:
		return (FICHA_JUGADOR_1) 
		
def definir_letras_posibles_segun_dimension_tablero():
	#OK
	"""Define según la dimensión del tablero, cúales son las letras válidas que podrán ser utilizadas por el usuario para indicar una posición. Considerando
	las letras de la A a la Z, la dimensión máxima del tablero será de 26x26."""
	letras_para_filas=LETRAS[:DIMENSION_TABLERO]
	return letras_para_filas
	
def convertir_fila_de_letra_a_numero(letras_para_filas, letra_de_fila):
	"""Recibe la variable letra_de_fila que representa la letra de la fila (en mayúscula) en la que el usuario desea colocar su ficha,y la devuelve convertida al 
	valor numérico correspondiente (número_de_fila). Es decir, para la A corresponderá el número 1, así sucesivamente hasta la Z que se corresponderá 
	con el número 26.""" 
	numero_de_fila=-1
	if letra_de_fila not in letras_para_filas:
		return -1
	else:
		for i in range (DIMENSION_TABLERO+1):
			while letras_para_filas[numero_de_fila]!=letra_de_fila:
				numero_de_fila+=1
		return numero_de_fila+1		
	
def posicion_dentro_de_rango(posicion):
	"""Dada la posición, determina que la misma sea válida, teniendo en cuenta si el usuario ingresó una fila y columna tal y como le fue 
	solicitado, es decir, que la misma esté dentro de las dimensiones del tablero (y no fuera de rango)."""
	numero_de_fila=posicion_elegida[0]
	numero_de_columna=posicion_elegida[1]
	if numero_de_fila<=DIMENSION_TABLERO and numero_de_fila>0 and int(numero_de_columna)<=DIMENSION_TABLERO:
		return True
		
def obtener_coordenadas_de_posicion(posicion,letras_para_filas):
	"""Recibe una variable str del tipo "letra-número", la separa y convierte en los correspondientes valores numéricos para fila y columna; devuelve
	las coordenadas de la posicion por separado como fila y columna."""
	letra_de_fila,numero_de_columna=posicion.split("-")
	letra_de_fila=letra_de_fila.upper()
	numero_de_fila=convertir_fila_de_letra_a_numero(letras_para_filas,letra_de_fila)
	return (int(numero_de_fila),int(numero_de_columna))

def solicitar_fila_y_columna():
	"""Le solicita al usuario que indique por consola cúal es la posición elegida para colocar su ficha de manera tal que se utilicen letras de la A 
	a la Z para indicar la fila, y números de 1 a 26 para indicar la columna (esto dependerá de la dimensión del tablero), separados por un guión (-). 
	Devuelve dos variables que indicarán el número de fila (numero_de_fila) y el número de columna (numero_de_columna) elegidos por el usuario para 
	colocar la ficha."""
	letras_para_filas=definir_letras_posibles_segun_dimension_tablero()
	while True:
		posicion_elegida=input("Por favor, indique la posición en la que desea colocar su ficha. Recuerde que deberá utilizar una letra de la A a la " 
		+ str(LETRAS[(DIMENSION_TABLERO)-1]) + " para indicar la fila, y un numéro de 1 a " + (str(DIMENSION_TABLERO)) + 
		" para indicar la columna, separados por un guión (LETRA-NÚMERO).   ")		
		numero_de_fila,numero_de_columna=obtener_coordenadas_de_posicion(posicion_elegida,letras_para_filas)
		posicion_elegida=(numero_de_fila,numero_de_columna)
		if posicion_dentro_de_rango(posicion_elegida):
			return (numero_de_fila,numero_de_columna)
		print("Usted ha ingresado una posición inválida.") 	

def calcular_puntajes_de_jugadores(tablero):
	"""Dada la variable que representa las fichas en el tablero, se contarán la cantidad de fichas negras (correspondientes al primer jugador); la cantidad se 
	devolverá en una variable (cantidad_fichas_negras) y lo mismo ocurrirá con la cantidad de fichas blancas (cantidad_fichas_blancas)."""
	cantidad_fichas_negras=0
	cantidad_fichas_blancas=0
	for i in range (0,DIMENSION_TABLERO*DIMENSION_TABLERO):
		if tablero[i]==FICHA_JUGADOR_1:
			cantidad_fichas_negras+=1
		elif tablero[i]==FICHA_JUGADOR_2:
			cantidad_fichas_blancas+=1
	return cantidad_fichas_negras,cantidad_fichas_blancas

def reportar_resultado_del_juego(Jugador_1, Jugador_2,cantidad_fichas_negras,cantidad_fichas_blancas):
	"""Imprime por pantalla el resultado final del juego con los puntajes de cada jugador. Recibe los nombres de los jugadores y las cantidades de fichas
	de cada uno de ellos"""
	if cantidad_fichas_blancas>cantidad_fichas_negras:
		print("El GANADOR es "+ Jugador_1 + " con " + str(cantidad_fichas_blancas) + " puntos.")
	if cantidad_fichas_blancas<cantidad_fichas_negras:
		print ("El GANADOR es "+ Jugador_2 + " con " + str(cantidad_fichas_negras) + " puntos.")
	if cantidad_fichas_blancas==cantidad_fichas_negras:
		print ("Se trata de un empate! Ambos jugadores terminaron la partida con "+ str(cantidad_fichas_blancas) + " puntos.")	
		
def obtener_numero_de_posicion(numero_de_fila,numero_de_columna):
	"""Dado el valor de la fila y de la columna, calcula el número que representa la posición en la lista tablero"""
	numero_de_posicion=((numero_de_fila)-1)*DIMENSION_TABLERO+((numero_de_columna)-1)
	return numero_de_posicion
		
	
		
def main:
	"""Se encargará de orquestar las funciones de manera tal que el juego Othello (también conocido como Reversi) pueda desarrollarse."""
	dar_bienvenida()
	entrada=preguntar_si_desea_comenzar_una_partida()	
		if entrada=="S":
			nombre_jugador_1,nombre_jugador_2=solicitar_nombres_jugadores()
			imprimir_tablero_inicial()
			tablero=generar_tablero()
			numero_de_jugada=1
			while numero_de_jugada<=60:
				
				(numero_de_fila,numero_de_columna)=solicitar_fila_y_columna()
				if hay_jugada_posible(numero_de_fila,numero_de_columna,tablero,ficha)==True:
					asignar_turno(numero_de_jugada)
					modificar_tablero(numero_de_fila,numero_de_columna,tablero,ficha)
					numero_de_jugada+=1
			reportar_resultado_del_juego()
			entrada=preguntar_si_desea_comenzar_una_partida()
		elif entrada.upper()=="N":
			quit()
		