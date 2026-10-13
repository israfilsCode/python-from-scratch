numbers = [1, 2, 3, 4, 5, 6, 7]

squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)

squares1 = [number ** 2 for number in numbers]
cubes = [number ** 3 for number in numbers]

print (squares1)
print(cubes)