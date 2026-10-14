class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def show_specs(self):
        print("CPU:", self.cpu)
        print("RAM:", self.ram)

class Developer:
    def __init__(self, name, computer):
        self.name = name
        self.computer = computer

    def show_info(self):
        print(self.name + "'s info:")
        self.computer.show_specs()


class AIEngineer(Developer):
    def __init__(self, name, computer, model):
        super().__init__(name, computer)
        self.model = model

    def show_info(self):
        super().show_info()
        print("AI model:", self.model)

    def build_model(self):
        print(self.name + " is building a " + self.model + " model")

class WebDeveloper(Developer):
    def __init__(self, name, computer, framework):
        super().__init__(name, computer)
        self.framework = framework

    def show_info(self):
        super().show_info()
        print("Framework", self.framework)

    def build_website(self):
        print(self.name + " is building a web application with " + self.framework)


computer1 = Computer("AMD Ryzen 3", "16GB")
computer2 = Computer("AMD Ryzen 7", "32GB")
computer3 = Computer("AMD Ryzen 9", "64GB")

developer1 = AIEngineer("Israfil", computer2, "Transformer")
developer2 = WebDeveloper("Dave", computer1, "Next.js")
developer3 = AIEngineer("Alice", computer3, "Neural Network")

developers = [
    developer1,
    developer2,
    developer3
]

for developer in developers:
    developer.show_info()

developer1.build_model()
developer2.build_website()