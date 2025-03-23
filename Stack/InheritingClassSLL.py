from SLL import *
class Stack(SLL):
    def __init__(self):
        super().__init__()
        self.count = 0
    def is_empty(self):
        return super().is_empty()
    def push(self, data):
        self.insert_at_start(data)
        self.count += 1
    def pop(self):
        if not self.is_empty():
            data = self.start.item
            self.delete_at_start()
            self.count -= 1
            return data
        else:
            raise IndexError("Stack is Empty")        
    def peek(self):
        if not self.is_empty():
            data = self.start.item
            return data
        else:
            raise IndexError("Stack is Empty")
    def size(self):
        return self.count
obj = Stack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
print("Top element of Stack is:", obj.peek())
print(f"Size of the stack is: {obj.size()}")
print(f"Remove element of the stack is: {obj.pop()}")
print("Top element of Stack is:", obj.peek())
print(f"Size of the stack is: {obj.size()}")