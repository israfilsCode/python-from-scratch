text = "I want to build an LLM from scratch"

print(text)
print("Number of characters:", len(text))

words = text.split()
print("Number of words:", len(words))

index = 0
for word in words:
    print(str(index) + ": " + word)
    index += 1

print("How many 'o's in text:", text.count('o'))

if "LLM" in text:
    print("LLM exists in text")
else:
    print("LLM doesn't exist in text")

print(text.replace("LLM", "language model"))