class Developer:
    allowed_languages = ["Python", "JavaScript", "Rust", "C++", "Go"]
    
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
            print("Invalid Language")

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

    def build_model(self):
        print(self.name + " is building a " + self.model + " model")

    def show_info(self):
        super().show_info()
        print("AI model:", self.model)


class WebDeveloper(Developer):
    def __init__(self, name, age, language, skills, framework):
        super().__init__(name, age, language, skills)
        self.framework = framework

    def build_website(self):
        print(self.name + " is building a web application with " + self.framework)

    def show_info(self):
        super().show_info()
        print("Framework:", self.framework)


developer1 = AIEngineer(
    "Israfil",
    21,
    "Python",
    ["Python", "Numpy", "PyTorch"],
    "Transformer"
)

developer2 = AIEngineer(
    "Alice",
    25,
    "Rust",
    ["Rust", "Python", "Scikit Learn"],
    "Neural Network"
)

developer3 = WebDeveloper(
    "Dave",
    19,
    "JavaScript",
    ["JavaScript", "React", "Node.js"],
    "Next.js"
)

developers = [developer1, developer2, developer3]

for developer in developers:
    developer.show_info()


developer1.build_model()
developer3.build_website()
