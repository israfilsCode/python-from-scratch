developer = {
    "name": "Israfil",
    "age": 21,
    "country": "Bangladesh",
    "role": "Software engineer",
    "language": "Python"
}

# for key in developer:
#     print(key + ": " + str(developer[key]))

for key, value in developer.items():
    print(key + ": " + str(value))