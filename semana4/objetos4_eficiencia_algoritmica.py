
#? Complejidad algoritmica -> Eficiencia entre dos algoritmos T(n)

"""la funcion factorial_r para que sea recursivo. Porque sino el codigo
habría dado error con 20000 iteraciones porque Python tiene un maximo
de 999 en “Recursion depth”.  He hecho unas pruebas y aqui os dejo
el codigo que utilizo yo:"""

import time
import sys

def factorial(n):
  response = 1

  while n > 1:
    response *= n
    n -= 1

  return response


def factorial_recursive(n):
  if n == 1:
    return 1

  return n * factorial_recursive(n - 1)


if __name__ == '__main__':
  n = 1000000
  sys.setrecursionlimit(n + 10)

  startingTime = time.time()
  factorial(n)
  endTime = time.time()
  print(f"Execturion time with bucle\t{endTime - startingTime}");

  startingTime = time.time()
  factorial_recursive(n)
  endTime = time.time()
  print(f"Execution time with recusive\t{endTime - startingTime}");





# from functools import reduce # para reducir un iterable a un solo valor, aplicando una función
# from operator import mul # mul es el operador *

# def factorial(n: int) -> int:
#    return reduce(mul, range(1, n + 1)) # o reduce(lambda x, y: x * y, range(1, n + 1))













"""
Hola, aquellos que tengan problemas al ejecutar el script realizado por el profesor:

Probablemente tu interprete de Python te este alertando:

maximum recursion depth exceeded in comparison

Esto se debe a que por seguridad Python tiene un limite de recursion (por defecto 1000, puedes leer más sobre ello en la documentación oficial de python) que puedes averiguar realizando en tu main() un:
"""
print(sys.getrecursionlimit())

"""
Antes de utilizarlo deberás hacer un import del modulo sys, al comienzo de tu script:

"""
import sys
"""
Para ampliar este limite debes hacer un:

"""
sys.setrecursionlimit(numero_limite=999999999991000000)
"""
De esta manera, la recursion funcionara hasta el limite especificado.
Pero, tal como especifica la documentación de Python, debes ser cuidadoso con aumentar este limite.
Espero haberlos ayudado,
Saludos!
"""