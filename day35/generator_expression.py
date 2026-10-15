
# List comprehension
numbers = [number * 2 for number in range(1, 6)]

# Generator Expression
squares = (x ** 2 for x in range(1, 6))

#  squares is generator

# print(next(squares))
# print(next(squares))
# print(next(squares))
# print(next(squares))

for number in squares:
    print(number)