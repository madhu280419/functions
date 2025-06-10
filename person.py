class Person:
    def __init__(self, traveller, driver):
        self.traveller = traveller
        self.driver = driver
    def details(self):
        print("Traveller: " + self.traveller + ", driver: " + self.driver)
tourists = Person(" Jaunty " , " Praveen")
tourists.details()