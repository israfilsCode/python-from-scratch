start = 1
end = 101
total_numbers = end - start
total = 0
total_even_count = 0
total_odd_count = 0
maximum = 0
minimum = start

for i in range(start, end):
    if i % 2 == 0:
        total_even_count += 1
    else:
        total_odd_count += 1

    if maximum < i:
        maximum = i

    if minimum > i:
        minimum = i

    total += i


average = total / total_numbers

print("Total:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Even numbers:", total_even_count)
print("Odd numbers:", total_odd_count)