"""
Tu tarea esta semana es adaptar la función costoTotal de tal forma que el primer parámetro que esta solicita #!(numeroPaquetes),
!En lugar de recibir un número, reciba una lista con la información de los paquetes.

*Esto implica que el ciclo que usas dentro de la función debe adaptarse también, además de que ya no será necesario tomar los datos de los paquetes por entrada estándar, ya que estos datos vienen en formato de diccionario dentro de la lista de paquetes.

Lee detenidamente el planteamiento del reto, cuando se te indique que hay que seguir un orden, es necesario que así sea. Sigue atentamente los pasos de la solución del reto si tienes dificultades al resolverlo. Planteamiento del reto Con respecto a la situación planteada, tendrás que tomar el código de la semana pasada y 
!adaptar la función costoTotal.
Para esto, reemplaza el parámetro numeroPaquetes por otro que tenga más sentido, por ejemplo, #!listaPaquetes.
?haz que el ciclo dentro de la función itere sobre la lista, tomando cada elemento de esta.
Los elementos dentro de la lista 
!son diccionarios cuyas llaves son: ALTO, ANCHO y PROFUNDO, 
?esto significa que ya NO se deberán tomar los datos como entrada estándar, en su lugar, 
!se usan los datos que vienen en cada diccionario que representa cada paquete.

#|$| lecciones de aprendizaje  
1. Identifica las variables que se quieren definir. 
2. Recordar de qué manera se pueden recolectar datos por entrada estándar para definir variables. 
3. Recordar el uso de estructuras iterativas.
4. Recordar el uso de funciones.
5. Recordar el concepto de estructura de datos.
6. Recordar el uso de diccionarios.  Solución del reto:
	|1. Toma el código de la semana pasada.
	|2. Cambia el nombre del parámetro numeroPaquetes por listaPaquetes, de la función costoTotal, es decir, la función debería ser costoTotal(listaPaquetes, descuento). 
	|3. Adapta el ciclo que usas dentro de la función, de tal forma que itere el parámetro listaPaquetes. Te recomendamos que uses un ciclo for. 
		>a. Cada elemento dentro de la lista es un diccionario que tiene como llaves ALTO, ANCHO y PROFUNDO, usa esas llaves para tomar el dato respectivo al alto, ancho y profundo. 
		>b. Envía los datos tomados a la función calcularCosto. 
		>c. El código restante es similar al del reto de la semana pasada.  
			-> #*Nota: Aquí se plantea lo estrictamente necesario que se debe de hacer para solucionar el reto en CodeRunner, sin embargo, te recomendamos que uses código adicional, impresiones de pantalla y demás elementos necesarios para resolverlo en tu computador. A la hora de entregar el código, solo pega las dos funciones, sin ninguna impresión de pantalla.
"""

# import json

# def read_json():
#   with open('archivo.json') as json_file:             #* <- Start open file
#     data = json.load(json_file)                       #* <- Read file generate variable data

#   # info_empresa = []                                 #? <- Create empty list
#   # info_empresa.append(data['NOMBRE_EMPRESA'])       #? <- Extract name company
#   # info_empresa.append(data["PAGINA_WEB"])           #? <- Extract web page

#   variable_paquetes = []
#   for paquetes in data['PAQUETES']:
#     variable_paquetes.append(paquetes)
#     # print('Alto: ' , paquetes['ALTO'])              #! <- Under the hood
#     # print('Ancho: ' , paquetes['ANCHO'])
#     # print('Profundo: ' , paquetes['PROFUNDO'])
#     # print('\n')
#   print("[#] Paquetes ->",len(variable_paquetes))     #* <- Print the number of packages

# if __name__ == '__main__':
#   read_json()

import json

def calcularCosto(alto, ancho, profundo):
	volumen = alto*ancho*profundo
	costo = volumen*5

	if alto > 30:
		costo = costo+float(2000)
	if costo > 10000:
		costo = costo+costo*0.19

	return costo


def costoTotal(numeroPaquetes, descuento):
	valtotal = 0
	total = 0

	for i in range(len(numeroPaquetes)):
		alto = numeroPaquetes[i]['ALTO']
		ancho = numeroPaquetes[i]['ANCHO']
		profundo = numeroPaquetes[i]['PROFUNDO']
		costo_total = calcularCosto(alto, ancho, profundo)
		total += costo_total
		valtotal = total - (total*descuento/100)
	return valtotal


if __name__ == '__main__':
	variable_paquetes = []

	def read_json():
		with open('reto_5_archivo.json') as json_file:             		#*<- Start open file
			data = json.load(json_file)                       		#*<- Read file generate variable data

		for paquetes in data['PAQUETES']:
			variable_paquetes.append(paquetes)

		return variable_paquetes

	read_json()
	print("[#] Paquetes ->",len(variable_paquetes))     	  #*-> Print the number of packages

	total = 0
	total += costoTotal(variable_paquetes, 10)
	print(total)

	#|$| test ->                                 
	# import json
	# with open('paquetes.json') as file:
	#     empresa = json.load(file)
	# print (costoTotal(empresa['PAQUETES'], 10))
	#|$| it should be -> 34492.5                  

	# print(calcularCosto(lista_paquets),descuento) 					#! it_should_be -()-> 34492.5
	# print(costoTotal(['PAQUETES'], 10)) 										#! it_should_be -()-> 34492.5






























#?reto5 ->
#|$| -> Limpieza de codigo para code rruner ->

def calcularCosto(alto, ancho, profundo):
	volumen = alto*ancho*profundo
	costo = volumen*5

	if alto > 30:
		costo = costo+float(2000)
	if costo > 10000:
		costo = costo+costo*0.19

	return costo


def costoTotal(numeroPaquetes, descuento):
	valtotal = 0
	total = 0

	for i in range(len(numeroPaquetes)):
		alto = numeroPaquetes[i]['ALTO']
		ancho = numeroPaquetes[i]['ANCHO']
		profundo = numeroPaquetes[i]['PROFUNDO']
		costo_total = calcularCosto(alto, ancho, profundo)
		total += costo_total
		valtotal = total - (total*descuento/100)
	return valtotal
#|$| <- Limpieza de codigo para code rruner <-

#|$| test ->                                 
import json
with open('reto_5_archivo.json') as file:
    empresa = json.load(file)
print (costoTotal(empresa['PAQUETES'], 10))
#|$| it should be -> 34492.5                  























# def read():
	# file = open("archivo.json", "r")        #// <- Start open file
	# archivo_json = file.read()              #// <- Read file
	# print(archivo_json)                     #// <- Print file
	# file.close()                            #!// <- End

"""
	#//? Ejecutar lineas?
	#// file = open("archivo.json", "r")        #// <- Start open file
	#// d = open(destino.csv, "w")              #// <- Open destination file
	#// linea = file.readline()

	#// while linea:
	#//   palabras = linea.split()
	#//   p = ";".join(palabras)
	#//   d.write(p)
	#//   d.write("\n")
	#//   print(p)
	#//   for palabra in palabras:
	#//     print(palabra)
	#//   linea = f.readline()
"""

# def generar_json_ej():          #! <- Example of generate json file
#   data = {}
#   data['clients'] = []
#   data['clients'].append({      #! <- Push a new client
#     'name': 'Juan',
#     'lastname': 'Perez',
#     'age': '20',
#     'amount': '100'
#   })
#   with open('data.json', 'w') as outfile:
#     json.dump(data, outfile, indent=4)

# if __name__ == '__main__':
	# read()                        #! <- Example of read file
	# generar_json_ej()             #! <- Example of generate json file
