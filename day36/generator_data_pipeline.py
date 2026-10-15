def even_numbers(n):
    evens_gen = (number for number in range(2, n + 1) if number % 2 == 0)

    return evens_gen

def squares(evens):
    for even in evens:
        yield even ** 2

square_evens = squares(even_numbers(20))

for square_even in square_evens:
    print(square_even)