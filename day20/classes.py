class Developer:
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role


developer = Developer("Israfil", 21, "Software Engineer")

print(developer)
print(developer.name)
print(developer.age)
print(developer.role)