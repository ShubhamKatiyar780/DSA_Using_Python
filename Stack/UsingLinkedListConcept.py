class Node:
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next
class Stack:
    def __init__(self, start = None):
        self.start = start
        self.item_count = 0
    def is_empty(self):
        return self.start == None
    def push(self, data):
        n = Node(data, self.start)
        self.start = n
        self.item_count += 1
    def pop(self):
        if not self.is_empty():
            data = self.start.item
            self.start = self.start.next
            self.item_count -= 1
            return data
        else:
            raise IndexError("Stack is Empty")
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Stack is Empty")
    def size(self):
        return self.item_count
obj = Stack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
print("Top element of Stack is:", obj.peek())
print(f"Size of the stack is: {obj.size()}")
print(f"Remove element of the stack is: {obj.pop()}")
print("Top element of Stack is:", obj.peek())