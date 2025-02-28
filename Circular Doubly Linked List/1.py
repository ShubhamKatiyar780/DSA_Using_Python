class Node:
    def __init__(self, prev = None, item = None, next = None):
        self.prev = prev
        self.item = item
        self.next = next
class CDLL:
    def __init__(self, start = None):
        self.start = start
    def is_empty(self):
        return self.start == None
    def insert_at_first(self, data):
        n = Node()
        n.item = data
        if self.is_empty():
            n.prev = n
            n.next = n
        else:
            n.prev = self.start.prev
            n.next = self.start
            self.start.prev.next = n
            self.start.prev = n
        self.start = n
    def insert_at_last(self, data):
        n = Node()
        n.item = data
        if self.is_empty():
            n.prev = n
            n.next = n
            self.start = n
        else:
            n.prev = self.start.prev
            n.next = self.start
            # self.start.prev.next = n
            n.prev.next = n
            self.start.prev = n
    def search(self, data):
        temp = self.start
        if temp is not None:
            while temp.next != self.start:
                if temp.item == data:
                    return temp
                temp = temp.next
            
            if temp.item == data:
                return temp
        return None
    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(temp, data, temp.next)
            temp.next.prev = n
            temp.next = n
    def print(self):
        temp = self.start
        if temp is not None:
            print(temp.item, end=' ')
            temp = temp.next
            while temp is not self.start:
                print(temp.item, end=' ')
                temp = temp.next

# -------------------OR-------------------
        # temp = self.start
        # if temp is not None:
            # while temp.next != self.start:
            #     print(temp.item, end=' ')
            #     temp = temp.next
            # print(temp.item)
list = CDLL()
list.insert_at_first(20)
list.insert_at_first(10)
list.insert_at_last(30)
list.insert_at_last(40)
list.print()
print(list.search(10))