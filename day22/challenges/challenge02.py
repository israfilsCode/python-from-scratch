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

    def change_language(self, new_language):

        allowed_languages = ["Python", "JavaScript", "C++", "Rust"]

        if new_language in allowed_languages:
            self.language = new_language
        else:
            print("Invalid language")


developer = Developer("Israfil", 21, "Python")

print(developer.age)

developer.change_age(22)

print(developer.age)

developer.change_age(-5)


developer.change_language("Rust")

print(developer.language)

developer.change_language("Banana")

print(developer.language)