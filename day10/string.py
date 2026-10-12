text = "I want to build an LLM from scratch"

print(text)
print(len(text))
print(text[0])
print(text[-1])
print(text.upper())
print(text.lower())

# Python strings are immutable, meaning you can't modify individual characters directly.
# For example, this would fail:
text[0] = "X"


# That's an important property we'll use later when working with text and tokenization.