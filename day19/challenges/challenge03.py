from functools import reduce

numbers = [2, 5, 8, 11, 14, 17, 20]

evens = list(filter(lambda number: number % 2 == 0, numbers))

square_evens = list(
    map(lambda number: number ** 2, evens)
)

total = reduce(lambda a, b: a + b, square_evens)

print(total)
