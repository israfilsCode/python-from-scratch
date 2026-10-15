squares = (x ** 2 for x in range(1, 11))

print(type(squares)) # <class 'generator'>

print(next(squares))  # 1
print(next(squares))  # 4
print(next(squares))  # 9
print(next(squares))  # 16
print(next(squares))  # 25

for square in squares:  # starting from 36  
    print(square) 


# You also demonstrated something particularly useful:
# print(next(squares))


# gave 1, then subsequent calls gave:
# 4
# 9
# 16
# 25

# Then your for loop continued from where the generator had paused:
# for square in squares:    print(square)


# so it started at:
# 36
# 49
# 64
# 81
# 100

# Excellent observation. ✅
