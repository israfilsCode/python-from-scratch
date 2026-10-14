class Developer:
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language

    def change_age(self, age):
        if age > 0:
            self.age = age
        else:
            print("Invalid age")


developer = Developer("Israfil", 21, "Python")

developer.change_age(22)

print(developer.age)