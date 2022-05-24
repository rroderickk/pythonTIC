
#? Conteo abstracto

def f(x):

  respuesta = 0.0
  
  for i in range(1000):
    respuesta += 1

  for i in range(x):
    respuesta += x

    for i in range(x):
      for j in range(x):
        respuesta += 1
        respuesta += 1

  return respuesta

print(f(100))

#|$| Crecimiento asintotico
# No importan variaciones pequeñas, el enfoque se centra en lo que pasa conforme el tamaño del problema se acerca al infinito
# Mejor de los casos, promedio, peor de los casos | Big O notation = problema de mayor tamaño, 

#! Ley de la suma
def g(n):
  for i in range(n):
    print(i)
  
  for i in range(n):
    print(i)
#? O(n) + O(n) = O(n+n) = O(2n) = O(n)


#! Ley de la suma
def s(n):
  for i in range(n):
    print(i)
  
  for i in range(n*n):
    print(i)
#? O(n) + O(n*n) = O(n+n^2) = O(n^2)


#! Ley de la multiplicacion
def m(n):
  for i in range(n):
    for j in range(n*n):
      print(i,j)
#? O(n) + O(n) = O(n*n) = O(n^2)


#! Recursividad multiple
def f(n):
  if n==0 or n==1:
    return 1
  return f(n-1) + f(n-2)
#? O(2**n)

#!  Un loop => crecimiento lineal.
#!  Un loop dentro de otro => crecimiento cuadratico
#!  Llamadas recursivas => crecimiento exponecncial.