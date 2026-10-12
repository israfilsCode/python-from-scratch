# 🚀 Day 10 — Challenge 1: String Processing
# Now let's start doing something closer to what you'll eventually need for an LLM.
# Given:

text = "I want to build an LLM from scratch"

print(text.count("o"))
print("LLM" in text)
print(text.replace("LLM", "language model"))

words = text.split()

print(words)
print("Number of words:", len(words))

# 🧠 Why this matters for your LLM goal
# You're starting to see the pipeline:
# Raw text
#    ↓
# String processing
#    ↓
# Split into pieces
#    ↓
# Tokens
#    ↓
# Numbers
#    ↓
# Neural network