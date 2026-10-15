def count_to_n(n):
    for i in range(1, n+1):
        yield i


for number in count_to_n(10):
    print(number)


# 🧠 Your mental model now
# count_to_n(10)
#       ↓
#    generator
#       ↓
#     yield 1
#       ↓
#     yield 2
#       ↓
#     yield 3
#       ↓
#     ...
#       ↓
#     yield 10