#leer un archivo linea por linea
#si está en la misma carpeta solo se referencia el nombre
with open('clase30.txt', 'r') as file:
    for lineas in file:
        print(lineas.strip()) #elimina los saltos de línea

#leer todas las lineas en una lista
with open('clase30.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

#añade al final información
with open('clase30.txt', 'a') as file:
    file.write("\n\nBy: ChatGPT")

#sobrescribir el texto
with open('clase30.txt', 'w') as file:
    file.write("\n\nBy: ChatGPT")


