class Node:
    def __init__(self, item = None, priority = None, next = None):
        self.item = item
        self.priority = priority
        self.next = next
class PriorityQueue:
    def __init__(self):
        self.start = None
        self.count = 0
    def is_empty(self):
        return self.count == 0
    def push_item(self, priority, data):
        n = Node(data, priority)
        
        # if self.start is None or priority < self.start.priority:
        # if not self.start or priority < self.start.priority:
        #     n.next = self.start
        #     self.start = n
        # else:
        #     temp = self.start
        #     while temp.next and temp.next.priority <= priority:
        #         temp = temp.next
        #     n.next = temp.next
        #     temp.next = n

#-----------------------------------OR-------------------------------------
        if self.start is None:
            self.start = n
        elif priority < self.start.priority:
            n.next = self.start
            self.start = n
        else:
            temp = self.start
            while temp.next is not None and temp.next.priority <= priority:
                temp = temp.next
            n.next = temp.next
            temp.next = n
        self.count += 1
    def pop_item(self):
        if self.start is None:
            raise IndexError ("Priority Queue is Empty")
        pop_data = self.start.item
        self.start = self.start.next
        self.count -= 1
        return pop_data
    def size(self):
        return self.count
obj = PriorityQueue()
obj.push_item(7, "Anchal")
obj.push_item(5, "Chauhan")
obj.push_item(3, "Katiyar")
obj.push_item(4, "Rishab")
obj.push_item(2, "Premanand")
obj.push_item(8, "Shubham")
obj.push_item(1, "Radha Rani")
print("Size of the Priority Queue is :", obj.size())
while not obj.is_empty():
    print(obj.pop_item())
print("Size of the Priority Queue is :", obj.size())