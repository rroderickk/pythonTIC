
# Decomposicion -> partir el problema en problemas mas pequeños

class Automovil:

  def __init__(self, modelo, marca, color):
    self.modelo = modelo
    self.marca = marca
    self.color = color
    self._estado = 'en_reposo'
    self._motor = Motor(cilindros=4)
    self._seguridad = AirBag()
    self._launch_control = Launch_Control()

  def accelerar(self, tipo='despacio'):
    if tipo == 'rapida': 
      self._motor.inyectar_gasolina(10)
    else: 
      self._motor.inyectar_gasolina(3)

    self._estado = 'en_movimiento'

  def desAccelerar(self, tipo):
    if tipo == "brusca":
        self._seguridad.activar()
    else:
      pass
  
  def lanzar_coche(self, tipo):
    if tipo == "lanzando":
        self._launch_control.activar()
    else:
      pass





class Motor:

  def __init__(self, cilindros, tipo='gasolina', nivelGasolina=46000, temperatura=0):
    self.cilindros = cilindros
    self.tipo = tipo
    self.temperatura = temperatura
    self.nivelGasolina = nivelGasolina
    self.estadoTemperatura = temperatura

  def accelerar(self, tipo):
    if tipo == "rapida":
      self._motor.inyectaGasolina(10)
      self._motor.temperatura(12)
    else: 
      self._motor.inyectaGasolina(3)
      self._motor.temperatura(7)
    self._estado = "EnMovimiento"

  def inyectar_gasolina(self, cantidad):
    self.temperatura += 1
    self.cantidad = cantidad
    self.nivelGasolina = self.nivelGasolina - cantidad

  def temperatura (self, grados):
    self.estadoTemperatura = self.estadoTemperatura + grados

  def informacion(self):
    print("\n")
    print(f"nivelGasolina = {self.nivelGasolina} y temperatura = {self.estadoTemperatura}")
    print("\n")


class Launch_Control:

  def __init__(self, estado="Lanzando"):
    self.estado = estado

  def activar(self):
    print("[WARNING: LAUNCH_CONTRO_ACTIVADO] Lanzando el vehiculo [!]...3...2...1")





class AirBag:

  def __init__(self, estado="optimo"):
    self.estado = estado

  def activar(self):
    print("SISTEMA DE SEGURAD DE CHOQUES ACTIVADO")
    self.estado = "inhalitado"



car1 = Automovil("AAFF","toyota", "rojo")
car1.lanzar_coche("lanzando")
car1._motor.informacion()
car1.accelerar("lenta")
car1._motor.informacion()
car1.desAccelerar("brusca")