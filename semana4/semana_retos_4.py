
# #? Semana 4 (@1)
# from datetime import datetime

# print("\nBienvenidos ---", datetime.today().strftime('%A %B %d, %Y %H:%M:%S'), "---\n")
# day = datetime.today().strftime('%A')

# #! <- fn =()=>
# def total_a_pagar(cantidad_integrantes, descuento, precio):
# 	return cantidad_integrantes * descuento * precio

# cantidad_de_integrantes = int(input("Ingrese la cantidad de integrantes: "))

# if day == "Saturday" or day == "Sunday":
# 	precio_total = total_a_pagar(cantidad_de_integrantes, descuento=1, precio=100)
# 	print(f"Total a pagar: ${precio_total}")
# 	#// print("$%d" % precio_total)
# else:
# 	precio_total = total_a_pagar(cantidad_de_integrantes, descuento=0.9, precio=40)
# 	print(f"Total a pagar: ${precio_total}")





# #? Semana 4 (@2)
# def maximun(a,b):
# 	max_value = 0
# 	if a > b:
# 		max_value = a
# 	else:
# 		max_value = b
# 	return print(max_value)
# maximun(4,5)
# maximun(5,4)







# #? Semana 4 (@3)
# string = 'Item 1,Item 2,Item 3,Item 4,Item 5'
# dos = int(string.split(',')[1].split(' ')[1]) 
# print(dos)






# #? Semana 4 (@4)
# def par_impar(numero_entero):
# 	if numero_entero % 2 == 0:
# 		print(numero_entero, "El numero es par")
# 		return True
# 	else:
# 		print(numero_entero, "El numero es impar")
# 		return False
# par_inpar(24)
# par_inpar(33)









# #? Semana 4 (@5)
# def peso_a_euro(peso):
# 	return peso / 4500
# print(peso_a_euro(10000))
# print(peso_a_euro(50000))











# #? Semana 4 (@RETO)
# Con respecto a la situación planteada, tendrás que tomar el código de la semana pasada y separarlo en dos funciones: calcularCosto(alto, ancho, profundo) y costoTotal(numeroPaquetes, descuento). Para esto, la primera función deberá contener el código que calcula el costo de un paquete, dado su volumen, tal como se venía trabajando la semana pasada, pero sin las impresiones en pantalla, la segunda función deberá solicitar los datos de cada paquete el número de veces que el parámetro numeroPaquetes indique, similar a la semana pasada, pero sin las impresiones en pantalla, con el añadido que esta vez hay que aplicarle un descuento proporcionado por el parámetro descuento. La función calcularCosto debe RETORNAR el costo del paquete, mientras que la función costoTotal deberá RETORNAR el costo acumulado de los paquetes que ha leído, con el descuento que se envíe como parámetro.

# #! Ejemplo anterior
# numeroPaquetes = int(input())
# costoTotal = 0

# for i in range(1, numeroPaquetes+1):
#     alto = float(input())
#     ancho = float(input())
#     profundo = float(input())

#     volumen = alto * ancho * profundo
#     costo = volumen*5

#     if alto > 30:
#             costo = costo + float(2000)

#     if costo > 10000:
#             costo = costo+costo*0.19
#     costoTotal = costoTotal + costo
#     print(volumen)
#     print(costo)
# print(costoTotal)

# Solución del reto

# 1. Crea una función llamada calcularCosto que reciba los siguientes parámetros, en el orden respectivo: alto, ancho, profundo.
# a. Dentro de esta función deberás poner el código que calcula el costo de un paquete, según su volumen.
# b. Asegúrate de NO imprimir nada.
# c. Retorna el costo del paquete, una vez ha sido calculado.
# 2. Crea una función llamada costoTotal que reciba los siguientes parámetros, en el orden respectivo: numeroPaquetes, descuento.
# a. Dentro de esta función, adapta el código cíclico de la semana pasada, de tal forma que este se ejecute numeroPaquetes veces.
# b. Quita el cálculo del costo de paquete individual, ya que ahora tienes una función que lo retorna.
# c. Usa la función calcularCosto para enviarle los parámetros de alto, ancho y profundo, que se deben de solicitar previamente por entrada estándar, y ve sumando lo que esta retorna en tu variable acumuladora de costo total.
# d. Asegúrate de NO imprimir nada.
# e. Calcula el descuento y aplicalo al costo total. #! Cual descuento?
# f. Retorna el nuevo costo total.

# |$| Solucion ------------------------------------>
# def calcularCosto(i, alto, ancho, profundo):
# 	volumen = alto * ancho * profundo
# 	costo = volumen * 5
# 	costo_del_paquete = float(0)
# 	if alto > 30:
# 		costo = costo + float(2000)
# 	if costo > 10000:
# 		costo = costo + costo * 0.19

# 	costo_del_paquete = costo_del_paquete + costo
# 	print('paq: ',i, costo_del_paquete)
# 	return costo_del_paquete


# def costoTotal(numeroPaquetes, descuento):
# 	total = 0
# 	for i in range(1, numeroPaquetes+1):
# 		alto = float(input("alto"))
# 		ancho = float(input("Ancho"))
# 		profundo = float(input("Prof"))
# 		costo_total = calcularCosto(i, alto, ancho, profundo)
# 		total += costo_total
# 	return total
# 	print("ct", total)

# #todo Response =(descuento?)=>
# numero_de_paquetes = int(input("inserte numero de paquetes a calcular"))
# solucion = costoTotal(numero_de_paquetes, 10)
# print(solucion)
# |$| Solucion <--------------------------------------------------------------------




#! Limpieza del codigo para el coderruner
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

	for i in range(numeroPaquetes):
		alto = float(input())
		ancho = float(input())
		profundo = float(input())
		costo_total = calcularCosto(alto, ancho, profundo)
		total += costo_total
		valtotal = total - (total*descuento/100)
	return valtotal

#! Response =()=>
# print(calcularCosto(35,10,5)) #* it_should_be =()=> 12792.5

