from DLL import *
class Deque:
    def __init__(self):
        self.mydeque = DLL()
        self.front = None
        self.rear = None
        self.count = 0
    def is_empty(self):
        return self.mydeque.is_empty()
    def check_empty(self):
        if self.is_empty():
            raise IndexError(("Deque is empty."))
    def add_front(self, item):
        self.mydeque.insert_at_start(item)
        self.front = self.mydeque.start.item
        if self.count == 0:
            self.rear = self.front
        self.count += 1
    def add_rear(self, item):
        self.mydeque.insert_at_last(item)
        temp = self.mydeque.start
        while temp.next is not None:
            temp = temp.next
        self.rear = temp.item
        if self.count == 0:
            self.front = self.rear
        self.count += 1
    def delete_front(self):
        self.check_empty()
        front_item = self.mydeque.start.item
        self.mydeque.delete_at_start()
        self.count -= 1
        if self.count == 0:
            self.front = self.rear = None
        else:
            self.front = self.mydeque.start.item
        return front_item
    def delete_rear(self):
        self.check_empty()
        rear_item = self.rear
        temp = self.mydeque.start
        while temp.next is not None:
            temp = temp.next
        if temp.prev:
            self.rear = temp.prev.item
        else:
            self.rear = None
        self.mydeque.delete_at_last()
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