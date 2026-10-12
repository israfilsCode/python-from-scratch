numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]

total = 0
minimum = numbers[0]
maximum = numbers[0]
total_even_count = 0
total_numbers = 0

for number in numbers:
    if (maximum < number):
        maximum = number
    if (minimum > number):
        minimum = number

    if number % 2 == 0:
        total_even_count += 1

    total_numbers += 1
    total += number


average = total / total_numbers

print("Total", total)
print("Average", average)
print("Maximum", maximum)
print("Minimum", minimum)
print("Number of even values", total_even_count)
    