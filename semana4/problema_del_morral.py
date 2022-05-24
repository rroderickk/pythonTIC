
#? Problema del morral (0one Knapsack problem)
# Morral de 15 kg, cual de los articulos me llevare?
# Cual retorna el mayor valor posible?
# Objetos: 12kg $4, 2kg: $2, 1kg: $1, 4kg: $10, 2kg: $2.

def morral(tamaño_morral, pesos, valores, nIndex):
  #! Caso base
  if nIndex == 0 or tamaño_morral == 0:
    return 0
  # print(f'Tamaño del morral: {tamaño_morral}, Peso: {pesos[nIndex - 1]}, Valores: {valores[nIndex - 1]}') #? <- Under the hood

  if pesos[nIndex - 1] > tamaño_morral:
    return morral(tamaño_morral, pesos, valores, nIndex - 1)
  
  maximo =  max(
    valores[nIndex - 1]
    + morral( tamaño_morral - pesos[nIndex - 1], pesos, valores, nIndex - 1),
    morral(tamaño_morral, pesos, valores, nIndex - 1)
  )
  # print(f'Maximo valor: {maximo}') #? <- Under the hood
  return maximo


if __name__ == '__main__':
  valores = [60, 100, 120]
  pesos = [10, 20, 30]
  tamaño_morral = 60
  nIndex = len(valores)

  resultado = morral(tamaño_morral, pesos, valores, nIndex)
  print(resultado)