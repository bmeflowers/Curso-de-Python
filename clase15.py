#uso de if para una condición
'''x = 10
if x > 5:
    print("x es mayor que 5.")
    print("Dentro del if")
elif x==5:
    print("X es igual a 5")
else:
    print("X es menor que 5")
print("Fuera del if")

#uso de if para mas de una condición
x = 15
y = 20

if x > 10 and y < 25:
    print("Se cumplen ambas condiciones")

if x > 10 or y < 25:
    print("Se cumplen una condición")

if not x > 10:
    print("X no es mayor que 10")'''

is_member = False
age = 2

if is_member:
    if age >= 15:
        print("Tienes acceso y eres miembro")
    else:
        print("Eres miembro pero no tienes acceso")
else:
    print("No eres miembro")



