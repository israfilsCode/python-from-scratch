numbers = [12, 45, 7, 23, 89, 34, 56]

search = int(input("Enter a number to search: "))

isFound = False

for number in numbers:
    if search == number:
        isFound = True
        break


if isFound:
    print("Found!")
else:
    print("Not found!")