from SLL import *
class Queue(SLL):
    def __init__(self, start=None):
        super().__init__(start)
        self.rear = None
        self.count = 0
    def is_empty(self):
        return super().is_empty()
    def enqueue(self, data):
        self.rear = data
        self.insert_at_last(data)
        self.count += 1
    def dequeue(self):
        if not self.is_empty():
            dequeue_item = self.start.item
            self.delete_at_start()
            self.count -= 1
            return dequeue_item
        else:
            return ("Queue is Empty")
    def get_rear(self):
        if not self.is_empty():
            return self.rear
        else:
            return ("Queue is Empty")
    def get_front(self):
        if not self.is_empty():
            return self.start.item
        else:
            return ("Queue is Empty")
    def size(self):
        return self.count
obj = Queue()
obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(30)
obj.enqueue(40)
print(f"Rear(First) Element of the Queue is: {obj.get_rear()}")
print(f"Front(Last) Element of the Queue is: {obj.get_front()}")
print(f"Size of the Queue is: {obj.size()}")
obj.enqueue(50)
print(f"Dequeue Element is: {obj.dequeue()}")
print(f"Rear(First) Element of the Queue is: {obj.get_rear()}")
print(f"Front(Last) Element of the Queue is: {obj.get_front()}")
print(f"Size of the Queue is: {obj.size()}")