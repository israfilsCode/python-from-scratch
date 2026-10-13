def analyze_numbers(numbers):
    total = 0
    maximum = numbers[0]
    minimum = numbers[0]
    even_count = 0
    odd_count = 0
    greater_than_10_count = 0
    positive_count = 0
    negative_count = 0
    zero_count = 0

    for number in numbers:
        if number > 0:
            positive_count += 1
        elif number < 0:
            negative_count += 1
        else:
            zero_count += 1

        if number > 10:
            greater_than_10_count += 1

        if maximum < number:
            maximum = number

        if minimum > number:
            minimum = number

        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

        total += number

    average = total / len(numbers)

    result = {
        "total": total,
        "average": average,
        "maximum": maximum,
        "minimum": minimum,
        "even_count": even_count,
        "odd_count": odd_count,
        "greater_than_10_count": greater_than_10_count,
        "positive_count": positive_count,
        "negative_count": negative_count,
        "zero_count": zero_count
    }

    return result



numbers = [-5, 10, -2, 7, 0, 15, -8]

result = analyze_numbers(numbers)

print(result)