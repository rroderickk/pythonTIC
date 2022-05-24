# Entornno virtual de Python

```py
$ python -m venv turtle 
# Activar el entorno virtual
turtle\Scripts\activate.bat
```
turtle.py
```py
import turtle
tortuga.forward(100)
tortuga.right(90)
turtle.done()
```

# Strings methods
```py
capitalize()	# Convierte el primer carácter en mayúsculas
casefold()	# Convierte una cadena en minúsculas
center()	# Devuelve una cadena centrada
count()	# Devuelve el número de veces que un valor especificado se produce en una cadena
encode()	# Devuelve una versión codificada de la cadena
endswith()	# Devuelve true si los extremos de cadena con el valor especificado
expandtabs()	# Establece el tamaño de la pestaña de la cadena
find()	# Busca la cadena de un valor especificado y devuelve la posición de donde fue encontrado
format()	# Formatos especifican los valores de una serie
format_map()	# Formatos especifican los valores de una serie
index()	# Busca la cadena de un valor especificado y devuelve la posición de donde fue encontrado
isalnum()	# Devuelve verdadero si todos los caracteres de la cadena son alfanuméricos
isalpha()	# Devuelve True si todos los caracteres de la cadena están en el alfabeto
isdecimal()	# Devuelve True si todos los caracteres de la cadena son decimales
isdigit()	# Devuelve verdadero si todos los caracteres de la cadena son dígitos
isidentifier()	# Devuelve True si la cadena es un identificador
islower()	# Devuelve verdadero si todos los caracteres de la cadena son minúsculas
isnumeric()	# Devuelve verdadero si todos los caracteres de la cadena son numéricos
isprintable()	# Devuelve verdadero si todos los caracteres de la cadena son imprimibles
isspace()	# Devuelve True si todos los caracteres de la cadena son espacios en blanco
istitle()	# Devuelve True si la cadena sigue las reglas de un título
isupper()	# Devuelve True si todos los caracteres de la cadena son mayúsculas
join()	# Se une a los elementos de un iterable al final de la cadena
ljust()	# Devuelve una versión justificada izquierda de la cadena
lower()	# Convierte una cadena en minúsculas
lstrip()	# Devuelve una versión de ajuste izquierdo de la cuerda
maketrans()	# Devuelve una tabla de traducción para ser utilizado en traducciones
partition()	# Devuelve una tupla donde la cadena se separó en tres partes
replace()	# Devuelve una serie en un valor especificado es reemplazado con un valor especificado
rfind()	# Busca la cadena de un valor especificado y devuelve la última posición de donde fue encontrado
rindex()	# Busca la cadena de un valor especificado y devuelve la última posición de donde fue encontrado
rjust()	# Devuelve una versión justificada derecha de la cadena
rpartition()	# Devuelve una tupla donde la cadena se separó en tres partes
rsplit()	# Divide la cadena en el separador especificado y devuelve una lista
rstrip()	# Devuelve una versión ajuste correcto de la cadena
split()	# Divide la cadena en el separador especificado y devuelve una lista
splitlines()	# Divide la cadena en los saltos de línea y devuelve una lista
startswith()	# Devuelve true si la cadena comienza con el valor especificado
strip()	# Devuelve una versión recortada de la cadena
swapcase()	# Permutas de los casos, se convierte en minúsculas mayúsculas y viceversa
title()	# Convierte el primer carácter de cada palabra en mayúsculas
translate()	# Devuelve una cadena traducida
upper()	# Convierte una cadena en mayúsculas
zfill()	# Rellena la cadena con un número determinado de valores de 0 a principios
```

# List methods
```py
Suma (+) Concatena dos o más listas:
a=[1,2]
b=[3,4]
a + b --> [1,2,3,4]

Multiplicación (*) Repite la misma lista:
a=[1,2]
a * 2 —> [1,2,1,2]

Añadir elemento al final de la lista:
a=[1]
a.append(2)=[1,2]

Eliminar elemento al final de la lista:
a=[1,2]
b=a.pop()
a=[1]

Eliminar elemento dado un indice:
a=[1,2]
b=a.pop(1)
a=[2]

Ordenar lista de menor a mayor, esto modifica la lista inicial
a=[3,8,1]
a.sort() —> [1,3,8]

Ordenar lista de menor a mayor, esto NO modifica la lista inicial
a=[3,8,1]
a.sorted() —> [1,3,8]

Eliminar elementos de lista Elimina el elemento de la lista dado su indice
a=[1,2,3]
del a[0] —> a[2,3]

Eliminar elementos de lista Elimina el elemento de la lista dado su valor
a=[0, 2, 4, 6, 8]
a.remove(6)
a=[0, 2, 4, 8]

Range creacion de listas en un rango determinado
a=(list(range(0,10,2))) -->crea un conteo desde 0 hasta 10 en pasos de 2 en 2.
a=[0,2,4,6,8]

Tamaño lista len Devuelve el valor del tamaño de la lista:
a=[0,2,4,6,8]
len(a)=5

list.append(x)

Agrega un ítem al final de la lista. Equivale a a[len(a):] = [x].

list.extend(iterable)

Extiende la lista agregándole todos los ítems del iterable. Equivale a a[len(a):] = iterable.

list.insert(i, x)

Inserta un ítem en una posición dada. El primer argumento es el índice del ítem delante del cual se insertará, por lo tanto a.insert(0, x) inserta al principio de la lista, y a.insert(len(a), x) equivale a a.append(x).

list.remove(x)

Quita el primer ítem de la lista cuyo valor sea x. Es un error si no existe tal ítem.

list.pop([i])

Quita el ítem en la posición dada de la lista, y lo devuelve. Si no se especifica un índice, a.pop() quita y devuelve el último ítem de la lista. (Los corchetes que encierran a i en la firma del método denotan que el parámetro es opcional, no que deberías escribir corchetes en esa posición. Verás esta notación con frecuencia en la Referencia de la Biblioteca de Python.)

list.clear()

Quita todos los elementos de la lista. Equivalente a del a[:].

list.index(x[, start[, end]])

Devuelve un índice basado en cero en la lista del primer ítem cuyo valor sea x. Levanta una excepción ValueError si no existe tal ítem.

Los argumentos opcionales start y end son interpetados como la notación de rebanadas y se usan para limitar la búsqueda a una subsecuencia particular de la lista. El index retornado se calcula de manera relativa al inicio de la secuencia completa en lugar de con respecto al argumento start.

list.count(x)

Devuelve el número de veces que x aparece en la lista.

list.sort(key=None, reverse=False)

Ordena los ítems de la lista in situ (los argumentos pueden ser usados para personalizar el orden de la lista, ve sorted() para su explicación).

list.reverse()

Invierte los elementos de la lista in situ.

list.copy()

Devuelve una copia superficial de la lista. Equivalente a a[:].

Un ejemplo que usa la mayoría de los métodos de lista:

list.clear()

```

# dir() en un diccionario encontré estos métodos
```py

clear(): Remueve todos los elementos del diccionario

copy(): Copia todos los elementos de un diccionario y los guarda en otra variable

fromkeys(): Crea un diccionario y sus llaves son los items de una secuencia

keys = ['a', 'b', 'c', 'd', 'e']

vowels = dict.fromkeys(keys) 

print(vowels)		# {'o': None, 'i': None, 'u': None, 'a': None, 'e': None}
get(): Devuelve el valor de una llave

items(): Devuelve una tupla con una lista de las llaves y valores del diccionario

sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

print(sales.items())		# dict_items([('apple', 2), ('orange', 3), ('grapes', 4)])

keys(): Lo mismo que items(), pero con solo las llaves de un diccionario
values(): Lo mismo que items(), pero con solo los valores

pop(key): remueve y retorna un elemento de un diccionario por su llave

popitem(): remueve y retorna un item(key, value) de un diccionario

setdefault(key, default_value): retorna un valor de una llave, si no lo encuentra inserta una llave con un valor en el diccionario

update([]): Recibe una secuencia key/value y actualiza el diccionario actual con el diccionario recibido

Recuerden para borrar elementos del diccionario:
.pop(‘keyName’) -->elimina el keyname
.popitem() --> elimina el ultimo item insertado
del your_Dic_Name[‘KeyName’] --> elimina el 'keyname’
del your_Dic_Name --> elimina por completo el diccionario creado
.clear() --> Vacia el diccionario
```



Jugando un poco con un iterador podemos usar la clase enumerate para saber la posición, la llave, y el valor de cada llave:

```py
for idx, key in enumerate(rae):
    print('{} : {} = {}'.format(idx, key, rae[key])) 
```




# Declaracion de tuplas
```py
a= 1,2,3
a=(1,2,3)
Operaciones con tuplas:
Acceder a un valor mediante indice de tupla
a[0]=1
Conteo de cuantas veces está un valor en la tupla
a.count(1)—>1

Declaración conjutos o Sets
a= set([1,2,3])
a={1,2,3}
Operaciones con conjuntos:

NO se puede acceder a un valor mediante índice
NO se puede agregar un valor ya existente, por ejemplo
Agregar un valor a conjunto
a.add(1)—> error!! (valor existente en set)
a.add(20)—> a={1,2,3,20}
Tenemos:
a={1,2,3,20}
b={3,4,5}
a.intersection(b)–> {3} (elementos en común)
a.union(b)—>{1,2,3,20,4,5} (elementos de a + b pero sin repetir ninguno)
a.difference(b)–>{1,2,20} (elementos de a que no se encuentran en b)
b.difference(a)–>{4,5} (elementos de b que no se encuentran en a)
```


### zip() la función zip lo que hace es regresar un iterador de tuplas.
```py
x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
list(zipped)
[(1, 4), (2, 5), (3, 6)]
```


# Comprehensions

List Comprehensions

```py
[element for element in element_list if element_meets_condition]
```

Dictionary Comprehensions

```py
{key: element for element in element_list if element_meets_condition}
```

Set Comprehensions

```py
{element for element in element_list if element_meets_condition}
```



# Ejemplo Comprehensions

```py
uid = [1, 2, 3]
students = ['John', 'Mary', 'Steve']
students_width_uid = { uid: student for uid, student in zip(uid, students)}

# students_width_uid -> {1: 'John', 2: 'Mary', 3: 'Steve'}
```


# random_numbers

```py
random_numbers =[]

for i in range(10):
  random_numbers.append(random.randint(1,3))

# random_numbers -> [2, 1, 1, 3, 3, 2, 3, 3, 1, 3]

non_repeated = {number for number in random_numbers}
# non_repeated -> {1, 2, 3}
```

# binary search
> para hacer una busqueda binaria se debe tener:
  - una lista
  - ordenar la lista
  - un valor a buscar
  - entonces la funcion recibe: la data(lista_ordenada), el valor a buscar, y el bajo y el alto de la lista

```py
import random                                         #! para generar numeros randomcos

def binary_search(data, target, low, high):
  if low > high:
    return False

  mid = (low + high) // 2                             #! <- Encontramos la mitad

  if target == data[mid]:                             #! <- Si el objetivo es la mitad = ya lo encontramos
    return True
  elif target < data[mid]:                            #! <- Si el objetivo es menor que la mitad, buscamos en la mitad izquierda
    return binary_search(data, target, low, mid - 1)
  else:                                               #! <- Si el objetivo es mayor que la mitad, buscamos en la mitad derecha
    binary_search(data, target, mid + 1, high)


if __name__ == '__main__':                            #! <- Entry point
  data = [random.randint(0, 100) for i in range(10)]  #! <- Generamos numeros random
  # sorted_data = sorted(data)
  data.sort()                                         #! <- Ordenamos la lista
  print(data)                                         #! <- Imprimimos la lista ordenada

  target = int(input('What number would you like to find? : ')) #! <- Pedimos el numero a buscar(objetivo)

  #? encontrado = binary_search(datos, objetivo, limite_bajo, limite_alto)
  found = binary_search(data, target, 0, len(data) - 1) #! <- Buscamos el objetivo en la lista
  print(found)                                          #! <- Imprimimos si lo encontramos o no
```

# Comma separated values
Manipulacion de archivos
  - fn open para leer archivos recibe dos parametros el primero es el nombre del archivo y el segundo es el modo de apertura
  - fn close para cerrar archivos y no tener problemas de memoria

```py
f = open('file.csv', 'r')
f = close()
```




# Decorators
Los decoradores permiten extender y modificar el funcionamiento de las funciones
los decoradores envuelven otra funcion que y permiten ejecutar codigo antes y despues
de que es llamada

```py
def decorator_function(original_function):
  def wrapper_function(*args, **kwargs):
    print('wrapper executed this before {}'.format(original_function.__name__))
    return original_function(*args, **kwargs)
  return wrapper_function

def lowe_case(func):
  def wrapper():
    result = func()
    return result.lower()
  return wrapper

def funcion_decoradora(funcion_parametro):
	def funcion_interior():
		print('Vamos a realizar un calculo: ')
		funcion_parametro()
		print('Hemos terminado el calculo')
	return funcion_interior

@funcion_decoradora
def suma():
	print(150 + 2220)

def resta():
	print(33 - 10)

```