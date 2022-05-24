import random

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


if __name__ == '__main__':
  data = [random.randint(0, 100) for i in range(10)]
  # sorted_data = sorted(data)
  data.sort()
  print(data)

  target = int(input('What number would you like to find? : '))

  #? encontrado = binary_search(datos, objetivo, limite_bajo, limite_alto)
  found = binary_search(data, target, 0, len(data) - 1)
  print(found)