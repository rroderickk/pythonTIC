
# Encapsulacion -> Ocultar o proteger detalles de implementacion
# Getters -> Obtener datos
# Setters -> Modificar datos

class CasillaDeVotacion:
  
  def __init__(self, identificador, pais):
    self._identificador = identificador
    self._pais = pais
    self._region = None

  @property
  def region(self):
    return self._region

  @region.setter
  def region(self, region):
    if region in self._pais:
      self._region = region
    else:
      raise ValueError(f'La region {region} no esta en la lista')


# casilla = CasillaDeVotacion(123, ['Mexico','Morelos'])
# print(casilla.region) # -> None

# casilla.region = 'Mexico'
# print(casilla.region) # -> Mexico










# Herencia -> Modelar jerarquia de clases, Permite compartir comportamiento comun

class Rectangulo:

  def __init__(self, base, altura):
    self._base = base
    self._altura = altura

  def area(self):
    return self._base * self._altura


rectangulo1 = Rectangulo(10, 20)
rectangulo1.area() # -> 200

rectangulo2 = Rectangulo(20, 20)
rectangulo2.area() # -> 400

rectangulo3 = Rectangulo(200000000, 20000000)
rectangulo3.area() # -> 40000000000


# |$| Heredando
class Cuadrado(Rectangulo):

  def __init__(self, lado):
    super().__init__(lado, lado)

cuadrado1 = Cuadrado(200000000)
cuadrado1.area() # -> 40000000000




# Polimorfismo -> Permite que una clase herede de otra, pero que pueda tener diferentes comportamientos
# Herencia: copy paste
# Polimorfismo: edit copy paste

class Persona:

  def __init__(self, nombre):
    self._nombre = nombre

  def avanzar(self):
    print(f'{self._nombre} avanzando')


class Ciclista(Persona):

  def __init__(self, nombre):
    super().__init__(nombre)

  def avanzar(self):
    print(f'{self._nombre} avanzando con dos ruedas')


if __name__ == '__main__':
  persona1 = Persona('Ana')
  persona1.avanzar() # -> Ana avanzando

  ciclista1 = Ciclista('Mariana')
  ciclista1.avanzar() # -> Mariana avanzando con dos ruedas



class Electronico:

  def __init__(self, nombre=None, precio=None, marca=None):
    self._nombre = nombre
    self._precio = precio
    self._marca = marca

  @property
  def nombre(self):
      return self._nombre

  @nombre.setter
  def nombre(self, nombre):
      self._nombre = nombre

  @property
  def precio(self):
    return self._precio

  @precio.setter
  def precio(self, precio):
    self._precio = precio

  @property
  def marca(self):
    return self._marca

  @marca.setter
  def marca(self, marca):
    self._marca = marca

  def Encendido(self):
    print(f"El dispositivo {self.nombre} se activo correctamente")


class Computadora(Electronico):

  def __init__(self,nombre, precio, marca, procesador = None, nucleos = None, t_grafica = None, m_board = None):
    super().__init__(nombre,precio,marca)
    self.procesador = procesador
    self._nucleos = nucleos
    self.t_grafica = t_grafica
    self.m_board = m_board

  @property
  def nucleos(self):
    return  self._nucleos

  @nucleos.setter
  def nucleos(self, nucleos):
    self._nucleos = nucleos

  def Encendido(self):
    print(f"Encendio la PC {self.nombre} con exito")

  def Tareas(self, nombre, n_nucleos):
    print(f"Esta realizando la tarea {nombre} con {n_nucleos}  nucleos asignados\n")

class Laptop(Computadora):

  def __init__(self,nombre, precio, marca):
    super().__init__(nombre,precio,marca)
    pass


if __name__ == '__main__':
  r2d2 = Electronico('R2 - D2', 999.999, '¿?')
  compu = Computadora('The Power',1000,'Varios','Core i5 5000', 4, 'gtx 1060', 'Aorus B450')
  lap = Laptop('RGB',1500,'MSI')

  r2d2.Encendido()
  print(f'Con precio de {r2d2.precio} y pertenece a {r2d2.marca}\n')

  compu.Encendido()
  print(f'Con precio de {compu.precio} con especificaciones {compu.procesador}, {compu.nucleos},\n '
        f'con una TG {compu.t_grafica} y una mother {compu.m_board}')
  compu.Tareas('Jugar Fornite',2)

  print(f'''{lap.nombre} {lap.precio} {lap.marca} {lap.procesador} {lap.nucleos} {lap.m_board}''')