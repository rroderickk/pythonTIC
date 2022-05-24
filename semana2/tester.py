# d/MM/aaaa

def fnEsMayor(p, e):
  casteadoParametro1 = int(p)
  casteadoParametro2 = int(e)

  if casteadoParametro1 > casteadoParametro2:
    print("\n\t [+] Test Passed ", casteadoParametro1, ">", casteadoParametro2, "\t ✔ \2")
    # return p,e
  else:
    print("\n\t[-] Test Failed ", casteadoParametro1, "<" , casteadoParametro2, "\t ✘ \4")
    # return p,e

def fnEsMenor(p, e):
  casteadoParametro1 = int(p)
  casteadoParametro2 = int(e)

  if casteadoParametro1 < casteadoParametro2:
    print("\n\t [+] Test Passed ", casteadoParametro1, ">", casteadoParametro2, "\t ✔ \2")
    # return p,e
  else:
    print("\n\t[-] Test Failed ", casteadoParametro1, "<" , casteadoParametro2, "\t ✘ \4")
    # return p,e



def fnEsperado(p, e):
  if p == e:
    print("\n\t[+] Test Passed ", p, "=", e, "\t ✔ \2")
    # return p,e
  else:
    print("\n\t[-] Test Failed ", p, "!=" , e, "\t ✘ \4")
    # return p,e


def tester(name, fn, *params,x="\3"):
  print("["+x+"] Iniciando Test: " + name)

  execution = fn(*params)
  print("\n\tResult: ", execution, "\n")

def main():
  tester("[1] Prueba de igualdad: ", fnEsperado, "prueba1", "prueba1", x="\1")
  tester("[2] Prueba de igualdad: ", fnEsperado, "test2", "diferente", x="\1")

  tester("[3] Prueba de >: ", fnEsMayor, "134", "1", x="\3")
  tester("[4] Prueba de <: ", fnEsMayor, 1, 13241, x="\3")

  tester("[5] Prueba de >: ", fnEsMenor, "134", "1", x="\4")
  tester("[6] Prueba de <: ", fnEsMenor, 1, 13241, x="\4")


if __name__ == '__main__':
  main()












  #!<- COLOR PRINTER ->
  # def colors_16(color_):
  #   return("\033[2;{num}m {num} \033[0;0m".format(num=str(color_)))


  # def colors_256(color_): #<- COLOR PRINTER
  #   num1 = str(color_)
  #   num2 = str(color_).ljust(3, ' ')

  #   if color_ % 16 == 0:
  #     return(f"\033[38;5;{num1}m {num2} \033[0;0m\n")
  #   else:
  #     return(f"\033[38;5;{num1}m {num2} \033[0;0m")

  # print("The 16 colors scheme is:")
  # print(' '.join([colors_16(x) for x in range(30, 38)]))
  # print("\nThe 256 colors scheme is:")
  # print(' '.join([colors_256(x) for x in range(256)]))
  #!<- COLOR PRINTER ->

