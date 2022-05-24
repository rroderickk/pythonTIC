
#? lineal search 
import random


def busqueda_lineal(lista, objetivo):
  match = False

  for elemento in lista:              #<- Complegidad algoritmica: O(n) #! lineal
    if elemento == objetivo:
      match = True
    break

  posicion = lista.index(objetivo)
  if posicion == True:
    return posicion

  return match, posicion


# if __name__ == '__main__':
  # tamaño_de_la_lista = int(input("De que tamaño será la lista: "))
  # objetivo = int(input("Que numero quieres encontrar? "))
  # lista = [random.randint(0, 100) for i in range(tamaño_de_la_lista)]

  # print(lista)
  # encontrado = busqueda_lineal(lista, objetivo)
  # print(f'El elemento {objetivo} {"esta" if encontrado else "no está"} en la lista su index es {encontrado[1]}')





#? binario search, need to sort the list



def busqueda_binaria(lista, bajo, alto, objetivo):
  print(f"Buscando {objetivo} entre {lista[bajo]} y {lista[alto - 1]}")

  if bajo > alto:
    return False, None

  mitad = (bajo + alto) // 2

  if lista[mitad] == objetivo:
    return True, mitad,

  if lista[mitad] < objetivo:
    return busqueda_binaria(lista, mitad + 1, alto, objetivo)
  # else:
  #   return busqueda_binaria(lista, bajo, mitad - 1, objetivo)
  return busqueda_binaria(lista, bajo, mitad - 1, objetivo)

if __name__ == '__main__':
  tamaño_de_la_lista = int(input("De que tamaño será la lista: "))
  objetivo = int(input("Que numero quieres encontrar? "))
  lista = [random.randint(0, 100) for i in range(tamaño_de_la_lista)]

  print(lista)
  encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
  print(f'El elemento {objetivo} {"esta" if encontrado else "no está"} en la lista su index es {encontrado}')
