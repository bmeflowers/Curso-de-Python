'''#factorial
def factorial (n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
factorial_5 = print("El factorial de 5 es: ", factorial(5))

def fibonacci (n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)
	
number = 7
print (fibonacci(number))'''

def nat (n):
	if n == 0:
		return 0
	else:
		return n + nat(n-1)
	
suma = print("La suma es: ", nat(5))


