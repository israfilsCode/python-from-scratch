with open("./notes.txt") as file:
    text = file.read()


print("Total characters:", len(text))

words = text.split()

print("Total words:", len(words))

print(str(text.count("I")) + " times 'I' appears")

print(str(text.count("Python")) + " times 'Python' appears")

if "LLM" in text:
    print("'LLM' exists in text")


index = 0
for word in words:
    print(str(index) + ": " + word)
    index += 1
