#iteradores

lista = [1, 2, 3 , 4]

#obtener el iterador
myIter = iter(lista)
#muestra que valores se van almacenando en memoria
print(next(myIter)) 
print(next(myIter)) 
print(next(myIter)) 
print(next(myIter)) 

#iterador en cadena
#cadena
text = ["Hola Mundo"]
#iterador
iter_text = iter(text)
#iterando la cadena
for char in iter_text:
    print(char)

#iterador para los numeros impares
#limite 
limit = 10
odd_iter = iter(range(1, limit+1,2)) 
#desde donde empieza, que itera y cada cuanto

#numeros impares
for num in odd_iter:
    print(num)
