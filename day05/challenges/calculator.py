def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))

addition = add(a, b)
subtraction = subtract(a, b)
multiplication = multiply(a, b)
division = divide(a, b)

print(str(a) + " + " + str(b) + " = " + str(addition))
print(str(a) + " - " + str(b) + " = " + str(subtraction))
print(str(a) + " * " + str(b) + " = " + str(multiplication))
print(str(a) + " / " + str(b) + " = " + str(division))