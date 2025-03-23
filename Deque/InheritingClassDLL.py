from DLL import *
class Deque(DLL):
    def __init__(self):
        super().__init__()
        self.front = None
        self.rear = None
        self.count = 0
    def is_empty(self):
        return super().is_empty()
    def check_empty(self):
        if self.is_empty():
            raise IndexError(("Deque is empty."))
    def add_front(self, data):
        self.insert_at_start(data)
        self.front = self.start.item
        if self.count == 0:
            self.rear = self.front
        self.count += 1
    def add_rear(self, data):
        self.insert_at_last(data)
        temp = self.start
        while temp.next is not None:
            temp = temp.next
        self.rear = temp.item
        if self.count == 0:
            self.front = self.rear
        self.count += 1
    def delete_front(self):
        self.check_empty()
        front_item = self.start.item
        self.delete_at_start()
        self.count -= 1
        if self.count == 0:
            self.front = self.rear = None
        else:
            self.front = self.start.item
        return front_item
    def delete_rear(self):
        self.check_empty()
        rear_item = self.rear
        temp = self.start
        while temp.next is not None:
            temp = temp.next
        if temp.prev is not None:
            self.rear = temp.prev.item
        else:
            self.rear = self.front = None
        self.delete_at_last()
        self.count -= 1
        return rear_item
    def get_front(self):
        self.check_empty
        return self.front
    def get_rear(self):
        self.check_empty
        return self.rear
    def size(self):
        return self.count
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