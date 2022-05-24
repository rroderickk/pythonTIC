
# Abstraccion -> Separar la informacion central de los detalles secundarios.

# |$| Lavadora
class Lavadora:

  def __init__(self):
    pass

  def lavar(self, temperatura=0):
    self._llenar_tanque_de_agua(temperatura)
    self._añadir_jabon()
    self._tiempo_de_lavado()
    self._lavar()
    self._centrifugar()
    self._notificar()
    self._auto_apagado()

  def _llenar_tanque_de_agua(self, temperatura):
    print("Llenando el tanque de agua a {} grados".format(temperatura))

  def _añadir_jabon(self):
    print("añadiendo jabon")
  
  def _tiempo_de_lavado(self, tiempo='1h'):
    print("tiempo de lavado por defecto {}".format(tiempo))

  def _lavar(self):
    print("Lavando la ropa")

  def _centrifugar(self):
    print("Centrifugando la ropa")
  
  def _notificar(self):
    print("La lavadora se ha terminado de lavar")

  def _auto_apagado(self):
    print("Apagando la lavadora")









# |$| Biblioteca
class Biblioteca:
  def __init__(self, nombre):
    self.nombre = nombre
    self._libros = []

  def consultar_nombre_biblioteca(self):
    return self.nombre

  def agregar_libro(self, libro):
    self._libros.append({
        libro.titulo,
        libro.autor,
        libro.cantidad_de_paginas,
        libro.genero,
        libro.sinopsis
    })

  def consultar_libros(self):
    return self._libros

  def consultar_libro(self, id):
    return self._libros[id]

  def quitar_libro(self, id):
    self._libros.pop(id)

class Libro:
  def __init__(self, titulo, autor, cantidad_de_paginas, genero, sinopsis):
    self.titulo = titulo
    self.autor = autor
    self.cantidad_de_paginas = cantidad_de_paginas
    self.genero = genero
    self.sinopsis = sinopsis

if __name__ == "__main__":
  whirpool = Lavadora()
  whirpool.lavar()

  biblioteca1 = Biblioteca("Aprende Python")
  print(biblioteca1.consultar_nombre_biblioteca())





# |$| Programa bibliotecario.
# while(ejecutar):
#   print("- - - B I B L I O T E C A S - - -")
#   opcion = int(input("¿Qué vas a hacer?:\n1-Crear Biblioteca\n2-Agregar libro\n3-Ver catalogo\n4-Quitar Libro\n5-Salir\n:"))
  
# if opcion == 1:
#     nombre = input("Nombre de la biblioteca: ")
#     biblioteca = Biblioteca(nombre)

#     print("Se creo la biblioteca: {}".format(biblioteca.consultar_nombre_biblioteca))

# elif opcion == 2:
#   titulo = input("Titulo: ")
#   autor = input("Autor: ")
#   cantidad_de_paginas = input("Paginas: ")
#   genero = input("Genero: ")
#   sinopsis = input("Sinopsis: ")

#   libro = Libro(titulo, autor, cantidad_de_paginas, genero, sinopsis)
#   biblioteca.agregar_libro(libro)

# elif opcion == 3:
#   print("Catalogo de libros: ")
#   for i in biblioteca.consultar_libros():
#     print(i)

# elif opcion == 4:
#   indice = input("Id del libro a eliminar: ")
#   biblioteca.quitar_libro(indice)

# elif opcion == 5:
#   ejecutar = False

# else:
#   print("Opcion incorrecta")

