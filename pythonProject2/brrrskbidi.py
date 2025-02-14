class Computer:
    def calculate(self):
        print('Calculate the task')

class Display:
    def display(self):
        print('On display 7 diamonds')

    def __init__(self, diag):
        self.diagonal = diag

class Smartphone(Computer, Display):
    pass

pocox7pro = Smartphone(mem = '64')