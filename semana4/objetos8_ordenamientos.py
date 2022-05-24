import random

#? Ordenamiento de burbuja (bubble sort) 
# Recorre repetidamente una lista que necesita ordenarse
# Comparamos cada elemento y si uno es mayor que otro lo vamos a intercambiar, iterando varias veces.

# def ordenamiento_de_burbuja(lista):
#   n = len(lista)

#   for i in range(n):
#     for j in range(0, n - i - 1): #* <- O(n) * O(n-) = O(n**2) crecimiento polinomial
#       if lista[j] > lista[j + 1]:
#         lista[j], lista[j + 1] = lista[j + 1], lista[j] #! <- swapping elements

#   return lista


# if __name__ == '__main__':
#   tamaño_de_la_lista = int(input("De que tamaño será la lista: "))

#   lista = [random.randint(0, 100) for i in range(tamaño_de_la_lista)]
#   print(lista)

#   lista_ordenada = ordenamiento_de_burbuja(lista)
#   print(lista_ordenada)






# #? Ordenamiento por inserción (insertion sort)
# """
# se evalua el primer elemento dentro la sublista desordenada para
# que podamos insertarlo en el lugar correcto dentro de la lista ordenada.

# La inserción se realiza al mover todos los elementos mayores al elemento que
# se está evaluando un lugar a la derecha.

# Continua el proceso hasta que la sublista desordenada quede vacia y, por lo
# tanto, la lista se encontrará ordenada.
# """


# def ordenamiento_por_insercion(lista):

#   for indice in range(1, len(lista)):
#     valor_actual = lista[indice]
#     posicion_actual = indice

#     while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
#       lista[posicion_actual] = lista[posicion_actual - 1]
#       posicion_actual -= 1

#     lista[posicion_actual] = valor_actual

# if __name__ == '__main__':
#   tamaño_de_la_lista = int(input("De que tamaño será la lista: "))

#   lista = [random.randint(0, 100) for i in range(tamaño_de_la_lista)]
#   print(lista)

#   lista_ordenada = ordenamiento_por_insercion(lista)
#   print(lista_ordenada)









#|$| Ordenamiento por mezcla (merge sort) y particiones
# Se divide la lista en dos partes, las cuales se ordenan recursivamente.
# Luego se mezclan las dos partes ordenadas.
# El proceso se repite hasta que la lista quede ordenada.

def ordenamiento_por_mezcla(lista):
  if len(lista) > 1:
    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]
    # print(izquierda, '*' * 5, derecha) #? <- Under the hood

    ordenamiento_por_mezcla(izquierda) #! <- O(n/2)  <- llamada recursiva
    ordenamiento_por_mezcla(derecha)   #! <- O(n/2) <- llamada recursiva

    #* Iteradores para recorrer las dos sublistas
    i = 0
    j = 0
    #* Iterador para la lista principal
    k = 0 

    while i < len(izquierda) and j < len(derecha):
      if izquierda[i] < derecha[j]:
        lista[k] = izquierda[i]
        i += 1
      else:
        lista[k] = derecha[j]
        j += 1
      k += 1

    while i < len(izquierda):
      lista[k] = izquierda[i]
      i += 1
      k += 1

    while j < len(derecha):
      lista[k] = derecha[j]
      j += 1
      k += 1
    # print(f"izquierda {izquierda}, derecha {derecha}") #? <- Under the hood
    # print(lista) #? <- Under the hood
    # print('-'*50) #? <- Under the hood
  return lista



if __name__ == '__main__':
  tamaño_de_la_lista = int(input("De que tamaño será la lista: "))

  lista = [random.randint(0, 100) for i in range(tamaño_de_la_lista)]
  print(lista)
  print('-' * 60)

  lista_ordenada = ordenamiento_por_mezcla(lista)
  print(lista_ordenada)