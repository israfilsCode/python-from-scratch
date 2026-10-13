numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(
    filter(lambda number: number % 2 == 0, numbers)
)

squares_evens = list(
    map(lambda number: number ** 2, evens)
)

print(squares_evens)