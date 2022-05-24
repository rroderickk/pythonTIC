intro = """
╔═╗┌─┐┌┐┌┬  ┬┌─┐┬─┐┌┬┐  ╦  ┬┌─┐ ┬ ┬┬┌┬┐
║  │ ││││└┐┌┘├┤ ├┬┘ │   ║  ││─┼┐│ ││ ││
╚═╝└─┘┘└┘ └┘ └─┘┴└─ ┴   ╩═╝┴└─┘└└─┘┴─┴┘ \n\t
[1] Opcion 1. Ml to L
[2] Opcion 2. L to Ml
"""

def main():
  print(intro)
  opcion = input("Insert your option: \n\t")


  if opcion == "1":
    quantity = input("Insert quantity mL: \n\t")
    print(float(quantity)/1000, " L")
  elif opcion == "2":
    quantity = input("Insert quantity L: \n\t")
    print(float(quantity)*1000, " mL")
  else:
    print("Invalid option", main())

if __name__ == '__main__':
  main()
