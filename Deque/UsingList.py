class Deque:
    def __init__(self):
        self.deque_list = []
    def is_empty(self):
        return len(self.deque_list) == 0
    def insert_front(self, data):
        self.deque_list.insert(0, data)
    def insert_rear(self, data):
        self.deque_list.append(data)
    def delete_front(self):
        if not self.is_empty():
            delete_front_item = self.deque_list[0]
            self.deque_list.pop(0)
            return delete_front_item
        return None
    def delete_rear(self):
        if not self.is_empty():
            delete_rear_item = self.deque_list[-1]
            self.deque_list.pop()
            return delete_rear_item
        return None
    def get_front(self):
        if not self.is_empty():
            return self.deque_list[0]
        return ("Deque is Empty")
    def get_rear(self):
        if not self.is_empty():
            return self.deque_list[-1]
        return ("Deque is Empty")
    def size(self):
        return len(self.deque_list)
obj = Deque()
obj.insert_front(20)
obj.insert_front(10)
obj.insert_front(5)
obj.insert_rear(30)
obj.insert_rear(40)
obj.insert_rear(50)
print(f"Size of the Queue is: {obj.size()}")
print(f"Rear(First) Element of the Queue is: {obj.get_rear()}")
print(f"Front(Last) Element of the Queue is: {obj.get_front()}")
print(f"Delete Rear Element is: {obj.delete_rear()}")
print(f"Delete Front Element is: {obj.delete_front()}")
print(f"Size of the Queue is: {obj.size()}")
print(f"Rear(First) Element of the Queue is: {obj.get_rear()}")
print(f"Front(Last) Element of the Queue is: {obj.get_front()}")