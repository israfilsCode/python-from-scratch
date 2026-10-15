with open("../notes.txt") as file:
    text = file.read()

print(text)

print(file.closed) # True