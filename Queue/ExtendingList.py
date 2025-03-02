class Queue(list):
    def is_empty(self):
        return len(self) == 0
    def enqueue(self, data):
        self.append(data)
    def dequeue(self):
        dequeue_item = self[0]
        self.pop(0)
        return dequeue_item
    def get_rear(self):
        if self.is_empty():
            return None
        return self[-1]
    def get_front(self):
        if self.is_empty():
            return None
        return self[0]
    def size(self):
        return len(self)
obj = Queue()
obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(30)
obj.enqueue(40)
obj.enqueue(50)
obj.enqueue(60)
print(f"Rear(First) Element of the Queue is: {obj.get_rear()}")
print(f"Front(Last) Element of the Queue is: {obj.get_front()}")
print(f"Size of the Queue is: {obj.size()}")
print(f"Dequeue Element is: {obj.dequeue()}")
print(f"Rear(First) Element of the Queue is: {obj.get_rear()}")
print(f"Front(Last) Element of the Queue is: {obj.get_front()}")
print(f"Size of the Queue is: {obj.size()}")