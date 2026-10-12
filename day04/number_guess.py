secret = 7

guess = int(input("Guess the number: "))

while secret != guess:
    if guess > secret:
        print("Too high!")
        guess = int(input("Guess the number: "))
    else:
        print("Too low!")
        guess = int(input("Guess the number: "))

print("Correct! 🎉")