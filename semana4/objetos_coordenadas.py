
# En python todo es un objeto y todo tiene un tipo, representacion en memoria y encapsulable.
# Generando tipos abstractos
"""
  #* Tenemos que definir una clase abstracta 
  ? @class
    class <nombre_clase>(<super_clase>)

  ? metodo __init__  =()=> constructor
    def __init__(self, <parametros>):
      <expresion || instrucciones>

    def <nombre_del_metodo>(self, <parametros>):
      <expresion || instrucciones>

  ! variable privada _PrivateVariable
"""

class Coordernada:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def ubicacion(self):
    print(f"N {self.x}, E {self.y}")
    return f"N {self.x}, E {self.y}"

#! ()=>
estoy_en = Coordernada(10, 20)
estoy_en_colombia = Coordernada(40, 40)



# |$| ->
class Coordenada_euclidiana:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def distancia(self, otra_coordenada):
    x_diff = (self.x - otra_coordenada.x) ** 2
    y_diff = (self.y - otra_coordenada.y) ** 2

    return (x_diff + y_diff) ** 0.5

coord_1 = Coordenada_euclidiana(3, 30)
coord_2 = Coordenada_euclidiana(4, 8)
print(coord_1.distancia(coord_2))





# |$| -> pitagoras
class Teorema_pitagoras(object):

  def __init__(self, cateto_1, cateto_2):
    self.cateto_1 = cateto_1
    self.cateto_2 = cateto_2

  def calculo_hipotenusa(self):
    hipotenusa = ((self.cateto_1**2)+(self.cateto_2**2))**0.5
    return hipotenusa




