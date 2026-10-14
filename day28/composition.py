class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram


class Developer:
    def __init__(self, name, computer):
        self.name = name
        self.computer = computer


computer = Computer("Ryzen 7", "16GB")
developer = Developer("Israfil", computer)

print(developer.computer.cpu)