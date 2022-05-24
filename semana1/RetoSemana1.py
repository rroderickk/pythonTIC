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

# def main():
#   print(intro)
#   height = float(input("[?] Insert height: \n") or 30)
#   width = float(input("[?] Insert width: ") or 30)
#   depth = float(input("[?] Insert depth: ") or 30)

#   volume = height * width * depth
#   result = volume*COST
#   print(result)

# if __name__ == '__main__':
#   main()


#|$| Reto1 clean code for the coderrunner:
alto = float(input())
ancho = float(input())
profundo = float(input()) 

volumen = alto * ancho * profundo
costo = volumen*6
print(volumen)
print(costo)

