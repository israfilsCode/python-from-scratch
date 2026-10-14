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


developer1.show_info()
developer2.show_info()
developer3.show_info()

developer3.change_language("Rust")

developer3.show_info()
