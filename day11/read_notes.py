# file = open("./notes.txt")

# text = file.read()

# print(text)
# print(len(text))

# file.close()



# But Python has a better pattern that automatically closes the file:

with open("./notes.txt") as file:
    text = file.read()

print(text)
print(len(text))