def count_to_n(n):
    for i in range(1, n + 1):
        yield i


def filter_divisible_by_n(numbers, n):
    for number in numbers:
        if (number % n == 0):
            yield number


def square_numbers(numbers):
    for number in numbers:
        yield number ** 2


numbers = count_to_n(100)

filtered_numbers = filter_divisible_by_n(numbers, 3)

squares = square_numbers(filtered_numbers)

for square in squares:
    print(square)