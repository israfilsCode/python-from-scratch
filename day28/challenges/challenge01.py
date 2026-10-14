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

    def show_setup(self):
        print(self.name)
        self.computer.show_specs()


computer = Computer("Ryzen 7", "16GB")
developer = Developer("Israfil", computer)

developer.show_setup()



# Inheritance vs Composition
# You now understand an important distinction:
# Inheritance — "is a"
# AIEngineer IS A Developer
# WebDeveloper IS A Developer

# Composition — "has a"
# Developer HAS A Computer
# Computer HAS A CPU/RAM

# In real software engineering, composition is extremely common because you can build complex systems by combining smaller objects.
# And this concept will eventually become very relevant when you build neural networks:
# NeuralNetwork
#    │
#    ├── has a → Layer
#    ├── has a → Layer
#    ├── has a → Layer
#    └── has a → Optimizer
