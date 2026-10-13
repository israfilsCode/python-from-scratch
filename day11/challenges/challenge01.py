with open("./notes.txt") as file:
    text = file.read()

print("Number of characters:", len(text))

words = text.split()
print("Number of words:", len(words))

if "Python" in text:
    print("Python exists in text")
else:
    print("Python doesn't exist in text")

if "LLM" in text:
    print("LLM exists in text")
else:
    print("LLM doesn't exist in text")

print("How many times 'I' appears:", text.count("I"))