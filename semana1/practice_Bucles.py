def main():
  LIMITE = 1000

  contador = 0
  potencia_2 = 2**contador
  while potencia_2 < LIMITE:
    print('2 elevado a ' + str(contador) + ' es igual a ' + str(potencia_2))

if __name__ == '__main__':
  main()