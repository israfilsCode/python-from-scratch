class Developer:
    def __init__(self, name, age, language, skills):
        self.name = name
        self.age = age
        self.language = language
        self.skills = skills

    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Language:", self.language)
        print("Skills:", self.skills)

    def show_skills(self):
        print(self.name + "'s skills:")
        for skill in self.skills:
            print(skill)



developer1 = Developer(
    "Israfil",
    21,
    "Python",
    ["Python", "JavaScript", "React", "PostgreSQL"]
)

developer2 = Developer(
    "Alice",
    25,
    "C++",
    ["C++", "Linux", "Networking"]
)

developer3 = Developer(
    "Dave",
    19,
    "JavaScript",
    ["JavaScript", "Node.js", "React"]
)

developers = sorted(
    [developer1, developer2, developer3],
    key=lambda developer: developer.age
)

for developer in developers:
    developer.show_skills()