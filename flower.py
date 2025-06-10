class flowers:
    def __init__(self, flower_1, flower_2):
        self.flower_1 = flower_1
        self.flower_2 = flower_2
    def details(self):
        flower_1 = "Jasmine"
        flower_2 = "Rose"
        my_flowers = flowers(flower_1, flower_2)
        print(my_flowers)
        my_flowers.details()
        