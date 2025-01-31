class Human:
    def __init__(self, name=None):
        self.name = name

    def __str__(self):
        return "Mister" + self.name


class Car:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = list()

    def add_passenger(self, pas):
        self.passengers.append(pas)

    def __str__(self):
        s = "Car: " + self.brand
        for pas in self.passengers:
            s += str(pas)
        return s


jack = Human('Jack')
page = Human('Larry')
taxi = Car('P.Didy car')
taxi.add_passenger(jack)
taxi.add_passenger(page)
taxi.add_passenger(Human('Bill'))
print(taxi.passengers)
