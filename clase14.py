#para diccionarios se usan llaves
#clave + valor
numbers = {1: "uno", 2:"dos", 3:"tres"}
print(numbers[2]) #se imprime el valor de esa clave
information = {"Nombre": "Allisson",
							"Apellido": "Pimentel",
							"estatura": 1.57,
							"Edad": 20}
print(information)
del information["Edad"]  #elimina ese dato
print (information)

#métodos propios de diccionarios
claves = information.keys()
print(claves)

values = information.values()
print(values)

pairs = information.items()
print(pairs)

contacts = {"Allisson": {"Apellido": "Pimentel",
						"Estatura": 1.57,
						"Edad": 20},
						"Lucy": {"Apellido": "Vargas",
						"Estatura:": 1.67,
						"Edad": 32}}
print(contacts["Allisson"])