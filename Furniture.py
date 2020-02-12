class Furniture:
    totalUnits = 0

    def __init__(self, name):
        self.name = name
        self.units = []
        print("This furniture is  {0}".format(self.name))

    def addUnit(self, unit):
        self.unit = unit
        self.units.append(unit)
        Furniture.totalUnits = Furniture.totalUnits + unit


furniture1 = Furniture("Table")
furniture2 = Furniture("Sofa")

furniture1.addUnit(25)
furniture1.addUnit(10)
furniture2.addUnit(35)
furniture2.addUnit(7)


print(furniture1)
print(furniture2)
print(Furniture.totalUnits)

print(furniture1.units)
print(furniture2.units)
