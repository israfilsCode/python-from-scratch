def analyze_numbers(numbers):
    total = 0
    maximum = numbers[0]
    minimum = numbers[0]
    evens_count = 0

    for number in numbers:
        if maximum < number:
            maximum = number

        if minimum > number:
            minimum = number

        if number % 2 == 0:
            evens_count += 1

        total += number

    average = total / len(numbers)

    result = {
        "total": total,
        "average": average,
        "maximum": maximum,
        "minimum": minimum,
        "evens_count": evens_count,
    }

    return result


numbers = [12, 45, 7, 23, 89, 34, 56]

result = analyze_numbers(numbers)

print(result)