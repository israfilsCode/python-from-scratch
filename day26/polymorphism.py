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
    def __init__(self, name, age, language, skills, model):
        super().__init__(name, age, language, skills)
        self.model = model

    def show_info(self):
        super().show_info()
        print("AI model:", self.model)

    def show_ai_info(self):
        print("AI model:", self.model)


class WebDeveloper(Developer):
    def __init__(self, name, age, language, skills, framework):
        super().__init__(name, age, language, skills)
        self.framework = framework

    def show_info(self):
        super().show_info()
        print("Framework:", self.framework)


ai_engineer = AIEngineer(
    "Israfil",
    21,
    "Python",
    ["Python", "NumPy", "PyTorch"],
    "Transformer"
)

web_developer = WebDeveloper(
    "Dave", 
    19, 
    "JavaScript", 
    ["JavaScript", "React", "Express.js"], 
    "Next.js"
)

developers = [ai_engineer, web_developer]

for developer in developers:
    developer.show_info()