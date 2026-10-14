class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def show_specs(self):
        print("CPU:", self.cpu)
        print("RAM:", self.ram)


class Editor:
    def __init__(self, name):
        self.name = name

    def open(self):
        print("Opening " + self.name)
    

class Developer:
    def __init__(self, name, computer, editor):
        self.name = name
        self.computer = computer
        self.editor = editor

    def start_work(self):
        print(self.name + " is starting work...")
        self.computer.show_specs()
        self.editor.open()


computer = Computer("Ryzen 7", "16GB")
editor = Editor("VS code")
developer = Developer("Israfil", computer, editor)

developer.start_work()