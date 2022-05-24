# #? Semana 4 (@5)

# string = "Tripulantes"
# string.replace()
# string.capitalize()
# string.split()
# string.upper()
# string.lower()

#! is_palindrome =()=>
#// import unicodedata
# def is_palindrome(word: str) -> str:
# 	word = word.lower() 				#* <- normalize.step1
# 	word = word.replace(" ", "") 		#* <- normalize.step2
# 	word = word.replace("á", "a") 		#* <- normalize.step3
# 	word = word.replace("é", "e") 		#* <- normalize.step3
# 	word = word.replace("í", "i") 		#* <- normalize.step4
# 	word = word.replace("ó", "o") 		#* <- normalize.step5
# 	word = word.replace("ú", "u") 		#* <- normalize.step6
# 	word = word.replace(":", "") 		#* <- normalize.step7
# 	word = word.replace(",", "") 		#* <- normalize.step8
# 	word = word.replace(";", "") 		#* <- normalize.step9
# 	word = word.replace("_", "") 		#* <- normalize.step10
# 	word = word.replace("\t", "") 		#* <- normalize.step511
# 	#// word = unicodedata.normalize('NFKD', word)
# 	#// word = word.encode('ASCII', 'ignore')

# 	drow = word[::-1]

# 	if word == drow:
# 		r = True
# 	else:
# 		r = False

# 	print(word, "=()=>", drow, ": ->", r,"\n")

# frase = ""
# while frase.lower().replace(" ", "") != 'salir':
# 	frase = input("[?] Ingrese una palabra o frase palíndromo \n[*] Para terminar el programa escriba 'salir' o Ctrl+c:\n")
# 	is_palindrome(frase)
# print("[!] Fin del programa")


#//  is_palindrome("luz azul")
#//  is_palindrome("luz azúl")
#//  is_palindrome("Anita lava la tina")
#//  is_palindrome("Anna")
#//  is_palindrome("hola")
#//  is_palindrome("reconocer")
#//  is_palindrome("2882288228822882")





# #? Semana 4 (@6)

# a = "Tripulante"
# b = 1234
# c = f"Hola {a}, codigo: {b}"
# d = "Hola {0}, codigo: {1}".format(a,b)
# print("Hola %s codigo: %d" % (a,b))






# #? Semana 4 (@7): listas
# lista = []
lista = [1,3,4]
lista2 = ["hola", "mundo", "!"]

lista2.append(1234) #* -> add element to the end of the list
lista2.pop(3) #* -> remove element from the end of the list
lista2.copy() #* -> return a copy of the list
lista2.remove("hola") #* -> remove element from the list
lista2.sort() #* -> sort the list
lista2.count(1234) #* -> return the number of elements in the list
lista2.reverse() #* -> reverse the list
lista2.extend(lista) #* -> add elements from the list
lista2.clear() #* -> remove all elements from the list

m = ("ingles,fisica,sociales,historia,programa")

def materias(m):
  cm = m.split(",")
  return cm

print(materias(m))



# #? Semana 4 (@8): listas

def listaFrutas(frutas):

  for fruta in frutas:
    print(fruta)

print(listaFrutas(["manzana", "pera", "uva", "naranja"])) # -> manzana, pera, uva, naranja


#// def listaFrutas(frutas):
#//   for fruta in range(len(frutas)):
#//     print(frutas(fruta))
#// list = ["manzana", "pera", "uva", "naranja"]
#// listaFrutas(list)

# #? Semana 4 (@8): listas

def multiplicarNumeros(lista):
  acumulador = 1
  for i in lista:
    acumulador *= i

  return acumulador

# print(multiplicarNumeros([2,3,5])) # -> 30
# print(multiplicarNumeros([2,2,2])) # -> 8
# print(multiplicarNumeros([2,3,4,5,6])) # -> 720



# #? Semana 4 (@9): Tuplas
# Se declaran con parentesis () -> Son inmutables

tupla = ()
tupla2 = (1,2,3)
tupla3 = ("hola", "mundo", "!")

tupla4 = ( "tupla4", 
  1234, 
  True, 
  (1,2,3,4), 
  [3,False,4],
  {"y":True,"x":False}
)


print("138",tupla4.count(True)) # -> 2
print("139",tupla4.index(True))









# #? Semana 4 (@10): Diccionarios
# Se declaran con parentesis {} -> Son inmutables

dc = {}
dc = dict()

dc1 = {"llave": "valor", "llave2": "valor2"}
dc2 = {"trip1": "rodri", "trip2": "juan", "trip3": "pedro"}

dc3 = { "nombre": "rodrigo", 
  "apellido": "mor",
  "edad": "23",
  "estado": True,
  "lista": [1,2,3,4],
  "tupla": (1,2,3,4),
  "diccionario": {"llave": "valor", "llave2": "valor2"},
  "diccionario2": {"llave": "valor", "llave2": "valor2"},
  "dinero": 0,
  "vivo": False,
}

dc3.keys() # -> return the keys of the dictionary
dc3.values() # -> return the values of the dictionary
dc3.items() # -> return the items of the dictionary
dc3.fromkeys(["llave", "llave2"], "valor") # -> return a dictionary with the keys and values
dc3.get("llave") # -> return the value of the key
dc3.popitem() # -> return the last item of the dictionary
dc3.update({"llave": "valor", "llave2": "valor2"}) # -> update the dictionary
dc3.copy() # -> return a copy of the dictionary
dc3.clear() # -> remove all elements from the dictionary
