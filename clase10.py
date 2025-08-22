to_do = ["Dirigirnos al hotel",
         "Almorzar",
         "Visitar un museo",
         "Volver al hotel"]
print(to_do)
numbers = [1, 2, 3, 4, "cinco"]
print(type(numbers))

mix = ["uno", 2, 3.14, True, [1, 2, 3, 4]]
print(mix)
print(len(mix))
print("Primer elemento", mix[0])
print("Segundo elemento", mix[1])
print("Ultimo elemento", mix[-1])
string = "Hola mundo"
print("Primer elemento",string[0])
print("Segundo elemento", string[1])
print("Ultimo elemento", string[-1])
print(mix[0:])

#método para agregar un elemento a la lista
print(mix)
mix.append(False)
print(mix)
mix.append(["u", "n", "o"])
print(mix)
mix.insert(1,["a", "b"])
print(mix)
print(mix.index(["a", "b"]))

#elemento mayor y menor
numbers = [1, 2, 100, 90.45, 3]
print("Mayor", max(numbers))
print("Menor", min(numbers))

#eliminar un elemento de la lista
del numbers[3]
print(numbers)

#porcion de elementos
del numbers[:4]
print(numbers)

#eliminar toda la lista
del numbers
print(numbers)