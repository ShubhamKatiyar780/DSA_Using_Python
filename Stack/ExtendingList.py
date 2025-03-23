class Stack(list):
    def is_empty(self):
        return len(self) == 0
    def push(self, data):
        self.append(data)
    def pop(self):
        if not self.is_empty():
            # return self.pop()          call of stack class / infinite recursion
            return super().pop()
        else:
            print("Stack is Empty")
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            print("Stack is Empty")
    def size(self):
        return len(self)
    # Restricting the use of the `insert` method
    def insert(self, index, data=None):  # overriding
        raise AttributeError("The 'insert' method is not allowed in Stack")
obj = Stack()
try:
    obj.insert(3, 50)  # Trying to use `insert`, which is not allowed
except AttributeError as e:  # Handle AttributeError instead of IndexError
    print(e)
obj.push(5)
obj.push(10)
obj.push(15)
obj.push(20)
print("Top element of Stack is:", obj.peek())
print(f"Size of the stack is: {obj.size()}")
print(f"Remove element of the stack is: {obj.pop()}")