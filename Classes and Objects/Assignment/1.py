class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f'Name: {self.name}, Age: {self.age}')

person1 = Person("John Doe", 30)
person1.show()
