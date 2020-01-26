def add(a,b):
	print(f"ADDING {a}+{b}")
	return a+b
def subtract(a,b):
	print(f"SUBTRACTING {a}-{b}")
	return a-b
def multiply(a,b):
	print(f"MULTIPLYING {a}*{b}")
	return a*b
def divide(a,b):
	print(f"DIVIDING {a}/{b}")
	return a / b
print("Let's do some math with just functions!")
age=add(30,5)
height=subtract(78,4)
weight=multiply(90,2)
iq=divide(100,2)
print(f"Age:{age}, Height:{height}, Weight:{weight}, IQ:{iq}")
print("Here's a puzzle.")
what=add(age,subtract(height,multiply(weight,divide(iq,2))))
print("That becomes:",what,"Can you do it by hand?")
print("The normal formula is:",
	"age+(height-(weight*iq/2))"
	"=",age+(height-(weight*iq/2)))
print("I am not sure what he means by a simple function, maybe something like (weight^2)/age?")
print(divide(multiply(weight,weight),age))
print("Or maybe he just means numbers, for example (10+4)/20")
print(divide(add(10,4),20))
