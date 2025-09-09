import os

cwd = os.getcwd()
print("Directorio de trabajo actual", cwd) #Current Working Directory

#Listar los archivos .txt
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Los archivos txt: ", txt_files)

#Renombrar archivo
os.rename('cuento.txt', 'cuento1.txt')
print('Archivo renombrado')

#Listar los archivos .txt
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Los archivos txt: ", txt_files)