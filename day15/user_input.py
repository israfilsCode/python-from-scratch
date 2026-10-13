def divide(a, b):
    return a / b

def get_number(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print("Invalid number. Try again.")
            continue


try:
    a = get_number("Enter number a: ")
    b = get_number("Enter number b: ")

    division = divide(a, b)

    print(division)

except ZeroDivisionError:
    print("Cannot divide by zero")