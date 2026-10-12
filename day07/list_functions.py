def find_max(numbers):
    maximum = numbers[0]

    for number in numbers:
        if maximum < number:
            maximum = number

    return maximum


numbers = [12, 45, 7, 23, 89, 34, 56]

maximum = find_max(numbers)

print(maximum)




def find_min(numbers):
    minimum = numbers[0]

    for number in numbers:
        if minimum > number:
            minimum = number

    return minimum


minimum = find_min(numbers)

print(minimum)