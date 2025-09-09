class Person:
	def __init__(self, name, age): #es una funcion propia de las clases, se definen los aatributos principales
		self.name = name
		self.age = age
	def saludar(self):
			print(f"Mi nombre es {self.name} y tengo {self.age} años.")
person1 = Person("Ana", 28)
person2 = Person("Luis", 43)

person1.saludar()
person2.saludar()