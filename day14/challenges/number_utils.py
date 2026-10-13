def is_even(number):
    return number % 2 == 0

def is_positive(number):
    return number > 0

def find_max(numbers):
    maximum = numbers[0]

    for number in numbers:
        if maximum < number:
            maximum = number

    return maximum

def find_min(numbers):
    minimum = numbers[0]

    for number in numbers:
        if minimum > number:
            minimum = number

    return minimum