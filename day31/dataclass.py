from dataclasses import dataclass

# class Computer:
#     def __init__(self, cpu, ram):
#         self.cpu = cpu
#         self.ram = ram

@dataclass
class Computer:
    cpu: str
    ram: str

    def show_specs(self):
        print("CPU:", self.cpu)
        print("RAM:", self.ram)


computer = Computer("Ryzen 7", "64GB")

computer.show_specs()