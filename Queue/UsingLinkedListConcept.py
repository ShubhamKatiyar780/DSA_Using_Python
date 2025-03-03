class Node:
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next
class Queue:
    def __init__(self, start = None):
        self.start = start
        self.rear = None
        self.count = 0
    def is_empty(self):
        return self.start == None
    def enqueue(self, data):
        n = Node(data)
        if self.is_empty():
            self.start = n
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        self.rear = data
        self.count += 1
    def dequeue(self):
        if not self.is_empty():
            dequeue_item = self.start.item
            self.start = self.start.next
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
print(f"Size of the Queue is: {obj.size()}")
print(f"Rear(First) Element of the Queue is: {obj.get_rear()}")
print(f"Front(Last) Element of the Queue is: {obj.get_front()}")
obj.enqueue(50)
print(f"Dequeue Element is: {obj.dequeue()}")
print(f"Size of the Queue is: {obj.size()}")        
print(f"Rear(First) Element of the Queue is: {obj.get_rear()}")
print(f"Front(Last) Element of the Queue is: {obj.get_front()}")