class Node:
    def __init__(self, item = None, prev = None, next = None):
        self.prev = prev
        self.item = item
        self.next = next
class Deque:
    def __init__(self, start = None):
        self.start= start
        self.front = None
        self.rear = None
        self.count = 0
    def is_empty(self):
        return self.start == None
    def check_empty(self):
        if self.is_empty():
            raise IndexError(("Deque is empty."))
    def add_front(self, data):
        n = Node(data, None, self.start)
        if not self.is_empty():
            self.start.prev = n
        self.start = n
        self.front = self.start.item
        if self.count == 0:
            self.rear = self.front
        self.count += 1
    def add_rear(self, data):
        n = Node(data, None, None)
        if self.is_empty():
            self.start = n
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
            n.prev = temp
        self.rear = temp.next.item
        if self.count == 0:
            self.front = self.rear
        self.count += 1
    def delete_front(self):
        self.check_empty()
        front_item = self.start.item
        self.start = self.start.next
        if self.start is not None:
            self.start.prev = None
        self.count -= 1
        if self.count == 0:
            self.front = self.rear = None
        else:
            self.front = self.start.item
        return front_item
    def delete_rear(self):
        self.check_empty()
        rear_item = self.rear
        if self.start.next is None:
            self.start = None
            self.rear = self.front = None
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            self.rear = temp.prev.item
            temp.prev.next = None
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