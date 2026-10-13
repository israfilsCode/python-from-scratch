def get_even_squares(numbers):
    even_squares = []

    for number in numbers:
        if number % 2 == 0:
            even_squares.append(number ** 2)

    return even_squares


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = get_even_squares(numbers)

print(result)