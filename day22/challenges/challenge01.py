class Developer:
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language

    def change_age(self, new_age):
        if new_age > 0:
            self.age = new_age
        else:
            print("Invalid age")


developer = Developer("Israfil", 21, "Python")

print(developer.age)

developer.change_age(22)

print(developer.age)

developer.change_age(-5)