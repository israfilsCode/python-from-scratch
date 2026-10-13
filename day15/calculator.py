try:
    a = int(input("Enter number a: "))
    b = int(input("Enter number b: "))

    print("Division:", a / b)
except ValueError:
    print("Invalid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
