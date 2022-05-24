mayor = """ 
╔═╗┌─┐┌─┐  ┌─┐┬  ┬┌─┐┬  ┬ ┬┌─┐┌┬┐┌─┐┬─┐
╠═╣│ ┬├┤   ├┤ └┐┌┘├─┤│  │ │├─┤ │ │ │├┬┘
╩ ╩└─┘└─┘  └─┘ └┘ ┴ ┴┴─┘└─┘┴ ┴ ┴ └─┘┴└─Says: dice:
----Continue to the party: Siga!----"""

menor = """
╔═╗┌─┐┌─┐  ┌─┐┬  ┬┌─┐┬  ┬ ┬┌─┐┌┬┐┌─┐┬─┐
╠═╣│ ┬├┤   ├┤ └┐┌┘├─┤│  │ │├─┤ │ │ │├┬┘
╩ ╩└─┘└─┘  └─┘ └┘ ┴ ┴┴─┘└─┘┴ ┴ ┴ └─┘┴└─Says: dice:
---- Access denied; No permitido el acceso a menores de edad! ----
---- Go home dont cry | Para tu casa chaval!----"""

intro = """
---- Welcome to the party of PythonRocker ----
╔═╗┌─┐┬─┐┌┬┐┬ ┬  ╦═╗┌─┐┌─┐┬┌─┌─┐┬─┐
╠═╝├─┤├┬┘ │ └┬┘  ╠╦╝│ ││  ├┴┐├┤ ├┬┘
╩  ┴ ┴┴└─ ┴  ┴   ╩╚═└─┘└─┘┴ ┴└─┘┴└─
---- No kids & No age minor & No permitido el acceso a menores de edad!----
---- Give me your AGE | Insert your AGE | Cual es tu edad? ----"""


def filtro(e):
  if e<18:
    print(menor)
  else:
    print(mayor)


def main():
  print(intro)
  age = input("Insert your age: \n\t")
  filtro(int(age))


if __name__ == '__main__':
  main()