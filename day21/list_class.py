class Developer:
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language

    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Language:", self.language)

    def change_language(self, language):
        self.language = language



developer1 = Developer("Israfil", 21, "Python")
developer2 = Developer("Alice", 25, "C++")
developer3 = Developer("Dave", 19, "JavaScript")

developers = [developer1, developer2, developer3]

for developer in developers:
    developer.show_info()