import sys,pdb,signal
import sys,pdb,signal
#Casting

# numero1 = input("Insert num here: ")
# numero2 = input("Insert second num here: ")

# print(int(numero1) + int(numero2))

# Logic Operators 

# es_Estudiante = True
# trabaja = False

# question1 = es_Estudiante or trabaja
# question2 = es_Estudiante and trabaja

# print(question1, question2)

# Money conversion
intro = """
┌─┐┌─┐┌┐┌┬  ┬┌─┐┬─┐┌┬┐┌─┐┬─┐
│  │ ││││└┐┌┘├┤ ├┬┘ │ ├┤ ├┬┘
└─┘└─┘┘└┘ └┘ └─┘┴└─ ┴ └─┘┴└─
1. COP to USD
2. ARG to USD
"""
print(intro)

opcion = input("Choose your option: ")

def conversor(cant, moneda)->float:
  return cant / moneda

money = float(input("Insert money here: "))
USD = 4000
ARG = 400

if opcion == '':
  print("You must choose an option")
  pass
elif opcion == '1':
  print(str(conversor(money, USD))+" USD")
  # pdb.set_trace() # <- breakpoint debugging
elif opcion == '2':
  print(str(conversor(money, ARG))+" ARG")
else:
  print("You must choose an option")


# Control C
def def_handler(sig, frame):
  print("\n\n[!] Exit...\n")
  sys.exit(1)

# Control C
signal.signal(signal.SIGINT, def_handler)




# Strings Methods
string = "Hola mundo"
# string.upper() #<- to upper
# string.lower() #<- to lower
# string.capitalize() #<- to capitalize
# string.title() #<- to title
# string.strip() #<- no spaces
# string = string.replace('a','i')
# string = string[0] + string[-1] + string[2:4] 
print(string)