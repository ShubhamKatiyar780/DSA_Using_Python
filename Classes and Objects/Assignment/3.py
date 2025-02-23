class Rectangle:
    def __init__(self, length, breadth):
        self.l = length
        self.b = breadth
    def setDimension(self, length, breadth):
        self.l = length
        self.b = breadth
    def showDimension(self):
        print(f"Length: {self.l}, Breadth: {self.b}")
    def getArea(self):
        return (self.l * self.b)
obj = Rectangle(5, 3)
obj.showDimension()
print(f"Area: {obj.getArea()}")

obj.setDimension(10, 4)
obj.showDimension()
print(f"Updated Area: {obj.getArea()}")