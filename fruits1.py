class Fruit:
    def __init__ (self, name, colour):
        self.name = name
        self.colour = colour
    def details(self):
        print(" My " + self.name + " is " + self.colour)
apple = Fruit("Apple", "red")
apple.details()