def count_number():
    yield 1
    yield 2
    yield 3


numbers = count_number()

print(next(numbers))
print(next(numbers))
print(next(numbers))