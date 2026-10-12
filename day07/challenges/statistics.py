def find_total(numbers):
    total = 0

    for number in numbers:
        total += number

    return total

def find_average(numbers):
    total = find_total(numbers)
    average = total / len(numbers)
    return average

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


def count_even(numbers):
    total_even_count = 0

    for number in numbers:
        if number % 2 == 0:
            total_even_count += 1

    return total_even_count



numbers = [12, 45, 7, 23, 89, 34, 56]

print("Total:", find_total(numbers))
print("Average:", find_average(numbers))
print("Maximum:", find_max(numbers))
print("Minimum:", find_min(numbers))
print("Even:", count_even(numbers))