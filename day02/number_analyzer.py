number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


if number % 2 == 0:
    print("Even")
else:
    print("Odd")


if number % 3 == 0:
    print("Divisible by 3")
else:
    print("Not divisible by 3")

if number % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")