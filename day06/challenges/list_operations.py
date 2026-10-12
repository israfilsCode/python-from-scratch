numbers = [10, 20, 30]

print(numbers)

numbers.append(40)
numbers.append(50)

numbers.pop()

print(numbers)

print(numbers[0])

last_index = len(numbers) - 1
print(numbers[last_index])

# One useful shortcut
# Python also supports negative indexing:
print(numbers[-1]) # this will give us last element
print(numbers[-2]) # this will give us second last element