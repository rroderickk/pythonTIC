Para los que se pregunten como se llego a ese resultado de forma matemática. aquí dejo mi aporte:
Primero empecemos con las definiciones:

class es una clase
def es una función, pero dentro de un class es un metodo, por lo tanto en nuestro ejemplo es un método.
constructor es el primer método que se ejecuta
instancia es lo que esta dentro de un método, después de self. Ejm.: (self, otra_coordenada).

```py
<code>
class Coordenada:
	def __init__(self, x, y):  #hasta aquí lo que esta después de self, solo son parametros.
		self.x = x
		self.y = y  
		# Aquí estamos inicializando las variables de instancia
```

luego escribimos el método que nos indica que hará el programa usando las instancias que se definieron en el constructor.

```py
<code>
def distancia(self, otra_coordenada):  #el parametro otra_coordenada es una instancia, que hara uso del molde en la primer clase de inicializacion, la cual usaremos despues, tomar atencion.
	x_diff = (self.x - otra_coordenada.x)**2
	y_diff = (self.y - otra_coordenada.y)**2

	return (x_diff +y_diff)**0.5
	#estos solo son una representación matemática de lo que hará el programa (lo explicare después)
```

luego tenemos que permitir que el programa corra desde nuestro terminal con:

```py
#mi caso yo prefiero usar comillas dobles, depende de ustedes.
if __name__ == "__main__": 
	coord_1 = Coordenada(3, 30)
	coord_2 = Coordenada(4, 8)
```
### Estas dos expresiones son instancias que usan el molde que es el primer método de inicializacion.
### luego para ver el output que nos arroja el programa corremos print, este print hace uso de la instancia con las clases.

```py
print(coord_1.distancia(coord_2))
#"coord_1" hace uso de la primer instancia, mientras que coord_2 al estar dentro del metodo distancia, ocupa el lugar de otra_coordenada. (entender esta parte es muy importante)
lo que vimos hasta ahora es la parte del código, pero matemáticamente pasa lo siguiente:
los parametros (x, y) en init son las ultimas instancias que definimos:
(3, 30) = (x, y) ------------------------- primer instancia
(4, 8) = (x, y) ------------------------- segunda instancia
```

ahora, recuerda que nuestro print fue:

```py
print(coord_1.distancia(coord_2))
coord_1 tomaria el lugar del primer metodo, es decir:
self.x = 3
self.y = 30
luego como coord_2 esta dentro del método distancia tomaría el lugar de la instancia “otra_coordenada” pero lo mas interesante es que esta instancia hace uso del molde en el primer método:
otra_coordenada.x = 4
otra_coordenada.y = 8
por tal motivo matemáticamente quedaría de la siguiente manera:
x_diff = (3 - 4)^2 = 1
y_diff = (30 - 8)^2 = 484

return (x_diff + y_diff)**0.5 quedaría de la siguiente manera:
(1 + 484)^(1/2) = 22.0227, su raiz cuadrada el resultado final.
```
