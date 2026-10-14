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



class AIEngineer(Developer):
    pass


ai_engineer = AIEngineer(
    "Israfil",
    21,
    "Python",
    ["Python", "NumPy", "Pytorch"]
)

ai_engineer.show_info()
ai_engineer.show_skills()