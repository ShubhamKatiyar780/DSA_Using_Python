class Stack:
    def __init__(self):
        self.item = []
    def is_empty(self):
        return len(self.item) == 0
    def push(self, data):
        self.item.append(data)
    def pop(self):
        if not self.is_empty():
            return self.item.pop()
        else:
            raise IndexError("Stack is Empty")
    def peek(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError("Stack is Empty")
    def size(self):
        return len(self.item)
obj = Stack()
print(obj.is_empty())
obj.push(10)
obj.push(20)
obj.push(30)
print("Top element of Stack is:", obj.peek())
print(f"Size of the stack is: {obj.size()}")
print(f"Remove element of the stack is: {obj.pop()}")