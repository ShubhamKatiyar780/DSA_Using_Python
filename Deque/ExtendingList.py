class Deque(list):
    def is_empty(self):
        return len(self) == 0
    def add_front(self, data):
        self.insert(0, data)
    def add_rear(self, data):
        self.append(data)
    def check_empty(self):
        if self.is_empty():
            raise IndexError("Deque is empty.")
    def delete_front(self):
        self.check_empty()
        front_item = self[0]
        self.pop(0)
        return front_item
    def delete_rear(self):
        self.check_empty()
        rear_item = self[-1]
        self.pop()
        return rear_item
    def get_front(self):
        self.check_empty()
        front_item = self[0]
        return front_item
    def get_rear(self):
        self.check_empty()
        rear_item = self[-1]
        return rear_item
    def size(self):
        return len(self)
obj = Deque()
obj.add_front(20)
obj.add_front(10)
obj.add_front(5)
obj.add_rear(30)
obj.add_rear(40)
obj.add_rear(50)
print(f"Size of the Queue is: {obj.size()}")
try:
    print(f"Rear(First) Element of the Queue is: {obj.get_rear()}")
except IndexError as e:
    print(e)
try:
    print(f"Front(Last) Element of the Queue is: {obj.get_front()}")
except IndexError as e:
    print(e)
try:
    print(f"Delete Rear Element is: {obj.delete_rear()}")
except IndexError as e:
    print(e)
try:
    print(f"Delete Front Element is: {obj.delete_front()}")
except IndexError as e:
    print(e)
print(f"Size of the Queue is: {obj.size()}")
try:
    print(f"Rear(First) Element of the Queue is: {obj.get_rear()}")
except IndexError as e:
    print(e)
try:
    print(f"Front(Last) Element of the Queue is: {obj.get_front()}")
except IndexError as e:
    print(e)