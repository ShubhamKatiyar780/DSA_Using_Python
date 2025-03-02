from SLL import *
class Queue:
    def __init__(self):
        self.myqueue = SLL()
        self.rear = None
        self.count = 0
    def is_empty(self):
        return self.myqueue.is_empty()
    def enqueue(self, data):
        self.myqueue.insert_at_last(data)
        self.rear = data
        self.count += 1
    def dequeue(self):
        if not self.is_empty():
            dequeue_item = self.myqueue.start.item
            self.myqueue.delete_at_start()
            self.count -= 1
            return dequeue_item
        else:
            return ("Queue is Empty")
    def get_rear(self):
        if self.is_empty():
            return None
        else:
            return self.rear
    def get_front(self):
        if self.is_empty():
            return None
        else:
            return self.myqueue.start.item
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
print(f"Dequeue Element is: {obj.dequeue()}")
print(f"Rear(First) Element of the Queue is: {obj.get_rear()}")
print(f"Front(Last) Element of the Queue is: {obj.get_front()}")
print(f"Size of the Queue is: {obj.size()}")