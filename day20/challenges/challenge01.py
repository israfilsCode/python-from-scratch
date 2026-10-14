class Developer:
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language


developer = Developer("Israfil", 21, "Python")

print("Name:", developer.name)
print("Age:", developer.age)
print("Language:", developer.language)