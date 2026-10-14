class Developer:
    allowed_languages = ["JavaScript", "Python", "Rust", "C++", "Go"] 
    def __init__(self, name, age, language, skills):
        self.name = name
        self.age = age
        self.language = language
        self.skills = skills

    def change_age(self, age):
        if age > 0 and age < 50:
            self.age = age
        else:
            print("Invalid age")

    def change_language(self, language):
        if language in self.allowed_languages:
            self.language = language
        else:
            print("Invalid language")

    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Language:", self.language)
        print("Skills:", self.skills)

    def show_skills(self):
        print(self.name + "'s skills:")

        for skill in self.skills:
            print(skill)


developer = Developer("Israfil", 21, "Python", ["Python", "JavaScript", "React", "PostgreSQL"])

developer.show_info()
developer.show_skills()
developer.change_age(22)
developer.change_age(-5)
developer.change_language("C++")
developer.change_language("Banana")

developer.show_info()