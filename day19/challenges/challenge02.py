from functools import reduce

numbers = [2, 3, 4, 5]

multiplication = reduce(lambda a, b: a * b, numbers)

print(multiplication)