def count_to_five():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


numbers = count_to_five()

print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
# print(next(numbers)) # raise en error StopIteration

for number in count_to_five():
    print(number)



# 🧠 The important distinction
# You now have:
# List
#  ↓
# Iterator
#  ↓
# Generator

# A list stores all its values:
# numbers = [1, 2, 3, 4, 5]


# A generator can produce them progressively:
# def numbers():    yield 1    yield 2    yield 3    yield 4    yield 5


# That's why generators become useful for large datasets.