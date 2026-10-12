# score = int(input("Enter your score: "))
# grade = None

# if score <= 100 and score >=90:
#     grade = "A"

# elif score >= 80:
#     grade = "B"

# elif score >= 70:
#     grade = "C"

# elif score >= 60:
#     grade = "D"

# elif score >= 0:
#     grade = "F"

# else:
#     grade = None


# if grade:
#     print("Grade: " + grade)
# else:
#     print("Invalid score")






# Cleaner version

score = int(input("Enter your score: "))

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")