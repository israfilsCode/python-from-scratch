numbers = [10, 20, 30, 40, 50]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# print(next(iterator)) raise an error StopIteration



# how for loop works behind the scene

numbers = [1, 2, 3, 4, 5]

iterator = iter(numbers)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
