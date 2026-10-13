numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# The pattern you want
# For filtering, the if goes at the end:

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)


# Read this almost like English:
# "Give me number for every number in numbers if the number is even."
