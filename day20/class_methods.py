class Developer:
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language

    def introduce(self):
        print("Hi, I am " + self.name)


developer = Developer("Israfil", 21, "Python")

developer.introduce()