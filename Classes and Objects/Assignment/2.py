class Circle:
    def __init__(self, radius):
        self.radius = radius
    def getRadius(self):
        return self.radius
    def setRadius(self, radius):
        self.radius = radius
    def getArea(self):
        return (3.14159 * self.radius**2)
    def getCircumference(self):
        return (2 * 3.14159 * self.radius)
    
obj = Circle(5)
print(f"Radius: {obj.getRadius()}")
print(f"Area: {obj.getArea()}")
print(f"Circumference: {obj.getCircumference()}")

obj.setRadius(10)
print(f"Updated Radius: {obj.getRadius()}")
print(f"Updated Area: {obj.getArea()}")
print(f"Updated Circumference: {obj.getCircumference()}")