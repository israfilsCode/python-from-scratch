def divide(a, b):
    return a / b

try:
    a = int(input("Enter number a: "))
    b = int(input("Enter number b: "))

    result = divide(a, b)

    print(result)
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")


# divide(10, 0)
#      ↓
# 10 / 0
#      ↓
# ZeroDivisionError
#      ↓
# returns to caller
#      ↓
# except ZeroDivisionError
#      ↓
# "Cannot divide by zero"

# That's an important concept: exceptions can propagate up the call stack.