
#? Reto 3 (@1)
# x = [ 1,4,None,2]
# for value in x:
# 	if value is not None:
# 		print(value)

#? Reto 3 (@2)
# i=0
# while i<9:
# 	if i<=3 or ( i>=6 and i<=8 ):
# 		print(i)
# 	i+=1

#? Reto 3 (@reto_semana_3)
#* 1. Crea una variable llamada numeroPaquetes y haz que esta lea un número entero.
#* 2. Crea una variable llamada costoTotal y asígnale como valor inicial cero.
#* 3.  Haz un ciclo for que se repita hasta numeroPaquetes.
#!  a. Dentro del ciclo, pon el código del reto anterior.
#!  b.  A la variable costoTotal súmale el costo del paquete de la iteración.
#* 4.  Imprime la variable costoTotal.

# numeroPaquetes = int(input())
# costoTotal = 0

# for i in range(1, numeroPaquetes+1):
# 	alto = float(input())
# 	ancho = float(input())
# 	profundo = float(input())

# 	volumen = alto * ancho * profundo
# 	costo = volumen*5

# 	if alto > 30:
# 		costo = costo + float(2000)

# 	if costo > 10000:
# 		costo = costo+costo*0.19
# 	costoTotal = costoTotal + costo
# 	print(volumen)
# 	print(costo)
# print(costoTotal)