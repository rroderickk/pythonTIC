
#? listas_tuplas_conjuntos_diccionarios

# def test1():
#   a = 1234
#   b = ["a", 3,True,6.6,a]
#   return a,b

# def test2():
#   a = 1234
#   b = ["a", 3,True,6.6,a]
#   c = b.append(a)
#   return a,b

# x,y = test1()
# c = test2()
# print("Primer variable: {} \nSegunda variable: {}\n3ra:{}".format(x,y,c))









#? Semana5 (@2 generador_de_contraseñas):
import random

def generar_numero_aleatorio(in_range):
  for i in range(in_range):
    contraseña = random.randint(1000,9999)
    print(contraseña)
  

def generador_contraseña_segura():
  letras_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  letras_minusculas = letras_mayusculas.lower()
  numeros = "1234567890"
  simbolos = "!@#$%^&*()_+-=<>?/.,;:[]{}|"
  contraseña = ""
  contraseña = contraseña + random.choice(letras_mayusculas)
  contraseña = contraseña + random.choice(letras_minusculas)
  contraseña = contraseña + random.choice(numeros)
  contraseña = contraseña + random.choice(simbolos)
  contraseña = contraseña + random.choice(numeros)
  contraseña = contraseña + random.choice(simbolos)
  return contraseña

#? Validando longitud
# def generar_contraseña_segura_desde_hasta():
#   contraseña = ""
#   longitud_minima = 8
#   longitud_maxima = 15
#   while len(contraseña) < longitud_minima or len(contraseña) > longitud_maxima:
#     contraseña = str(input("Ingrese su contraseña: "))
#   if len(contraseña) >= longitud_minima and len(contraseña) <= longitud_maxima:
#     return contraseña

def generar_contraseña_segura(n=12):
  contraseña = ""
  for i in range(n):
    caracter_aleatorio = random.choice(
      "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    )
    contraseña += caracter_aleatorio
  return contraseña


# def separar_string():
#   string = "Estoesunapruebadestring"
#   list = []
#   for char in string:
#     list.append(char)
#   return list

# def separar_string():
#   string = "Estoesunapruebadestring"
#   list = []
#   for i in range(len(string)):
#     list.append(string[i:i+1])
#   return list

# def separar_string():
#   string = "Estoesunapruebadestring"
#   list = []
#   while len(string) > 0:
#     list.append(string[:1])
#     string = string[1:]
#   return list


def generar_hases(n=4):
  return generar_contraseña_segura(n)


def generar_hashes_list():
  hashes = {}
  for i in range(4):
    hashes[generar_contraseña_segura()] = "La contraseña es segura"
  return hashes


if __name__ == '__main__':
  # print(separar_string())
  # print(f"{generador_contraseña_segura()}-{generar_contraseña_segura()}")
  # print(f"{generar_hases()}-{generar_hases()}-{generar_hases()}")
  # print(f"{generar_hases(20)}-{generar_hases(20)}-{generar_hases(20)}")
  # print(f"{generar_hases(14)}-{generar_hases(14)}-{generar_hases(14)}")
  print(f"{generar_hashes_list()}-{generar_hashes_list()}-{generar_hashes_list()}")
