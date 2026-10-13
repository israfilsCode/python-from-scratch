numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)

# another way of doing this

squares1 = list(map(lambda number: number ** 2, numbers))

print(squares1)