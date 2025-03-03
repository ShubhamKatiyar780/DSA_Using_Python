class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def enqueue(self, data):
        self.items.append(data)
    def dequeue(self):
        if not self.is_empty():
            dequeue_item = self.items[0]
            # self.items.remove(self.items[0])
            self.items.pop(0)
            return dequeue_item
        else:
            return ("Queue is Empty")
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        return None
    def size(self):
        return len(self.items)
obj = Queue()
obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(30)
obj.enqueue(40)
print(f"Size of the Queue is: {obj.size()}")
print(f"Rear(First) Element of the Queue is: {obj.get_rear()}")
print(f"Front(Last) Element of the Queue is: {obj.get_front()}")
print(f"Dequeue Element is: {obj.dequeue()}")
print(f"Rear(First) Element of the Queue is: {obj.get_rear()}")
print(f"Front(Last) Element of the Queue is: {obj.get_front()}")
print(f"Size of the Queue is: {obj.size()}")