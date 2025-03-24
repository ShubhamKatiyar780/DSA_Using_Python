class PriorityQueue:
    def __init__(self):
        self.pqueue = []
    def is_empty(self):
        return len(self.pqueue) == 0
    def push_item(self, priority, data):
        index_no = 0
        while index_no < len(self.pqueue) and self.pqueue[index_no][0] <= priority:
            index_no += 1
        self.pqueue.insert(index_no, (priority, data))
    def pop_item(self):
        if self.is_empty():
            raise IndexError("Priority Queue is Empty")
        return self.pqueue.pop(0)[1]
    def siz(self):
        return len(self.pqueue)
obj = PriorityQueue()
obj.push_item(7, "Anchal")
obj.push_item(5, "Chauhan")
obj.push_item(3, "Katiyar")
obj.push_item(4, "Rishab")
obj.push_item(2, "Premanand")
obj.push_item(6, "Shubham")
obj.push_item(1, "Radha Rani")
while not obj.is_empty():
    print(obj.pop_item())