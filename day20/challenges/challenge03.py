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


developer = Developer("Israfil", 21, "Python")

developer.change_language("C++")

developer.show_info()