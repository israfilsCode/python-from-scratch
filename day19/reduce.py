from functools import reduce

numbers = [1, 2, 3, 4, 5]

sum_of_numbers = reduce(lambda a, b: a + b, numbers)

print(sum_of_numbers)