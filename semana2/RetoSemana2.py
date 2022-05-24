intro = """
---- Welcome Sr----
╦═╗┌─┐╦═╗┌─┐┌─┐┬┌┬┐┌─┐
╠╦╝├┤ ╠╦╝├─┤├─┘│ │││ │
╩╚═└─┘╩╚═┴ ┴┴  ┴─┴┘└─┘
---- Cost per Package --- 
--- Depends of volume ---
--- Price to customer depends of: Volumen*5  ---\n\n
"""

COST = 5

def main():
  print(intro)
  height = float(input("[?] Insert height: ") or 30)
  width = float(input("[?] Insert width: ") or 10)
  depth = float(input("[?] Insert depth: ") or 10)

  volume = height * width * depth
  result = volume * COST

  if height > 30:
    result = result + 2000
  if result > 10000:
    iva = result * 0.19
    priceWitIva = result+iva
    print("Volume package: {} Price with IVA(19%): ${} ".format(volume, priceWitIva))
  else:
    print("Volume package: {} Price: ${}".format(volume, result))


if __name__ == '__main__':
  main()


#* Reto1:
# alto = float(input())
# ancho = float(input())
# profundo = float(input())

# volumen = alto * ancho * profundo
# costo = volumen*6 #!<-   CASCARITA 
# print(volumen)
# print(costo)



#? Reto2:
# alto = float(input())
# ancho = float(input())
# profundo = float(input())

# volumen = alto * ancho * profundo
# costo1 = volumen*5
# print(volumen)

# if alto > 30:
#   costo1 = costo1 + 2000

# if costo1 > 10000:
#   iva = costo1 * 0.19
#   costo2 = costo1 + iva
#   print(costo2)

# else:
#   print(costo1)
