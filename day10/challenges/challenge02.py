text = "I want to build an LLM from scratch"

words = text.split()

index = 0
for word in words:
    print(str(index) + ": " + word)
    index += 1