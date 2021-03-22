from src.randomFunctions.randomItemFromList import randomItemFromList

class randomItemsFromList(randomItemFromList):
    def __init__(self, array, n):
        super().__init__(array)
        self.genItems = []
        self.n = n
        self.generateChoices()

    def generateChoices(self):
        if self.n > len(self.array):
            self.genItems = "ERROR: n is greater then array size"
        else:
            for i in range(self.n):
                super().generateChoice()
                self.genItems.append(super().getValue())
                self.array.remove(super().getValue())

    def getValue(self):
        return self.genItems