class Node:
    def __init__(self, item = None, prev = None, next = None):
        self.item = item
        self.prev = prev
        self.next = next
class CDLL:
    def __init__(self, start = None):
        self.start = start
    def is_empty(self):
        return self.start == None
    def insert_at_first(self, data):
        n = Node(data)
        if self.is_empty():
            n.prev = n
            n.next = n
        else:
            n.prev = self.start.prev
            n. next = self.start
            self.start.prev.next = n
            self.start.prev = n
        self.start = n
    def insert_at_last(self, data):
        n = Node(data)
        if self.is_empty():
            n.prev = n
            n.next = n
            self.start = n
        else:
            n.prev = self.start.prev
            n.next = self.start
            self.start.prev.next = n
            # n.prev = n
            self.start.prev = n
    def search(self, data):
        if not self.is_empty():
            temp = self.start
            while temp.next != self.start:
                if temp.item == data:
                    return temp
                temp = temp.next
            if temp.item == data:
                return temp
            return None
        return None
    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(data, temp, temp.next)
            temp.next.prev = n
            temp.next = n
    def print(self):
        temp = self.start
        if temp is not None:
            while temp.next != self.start:
                print(temp.item, end=' ')
                temp = temp.next
            print(temp.item)
    def delete_at_first(self):
        if self.start is not None:
            if self.start == self.start.next:
                self.start = None
            else:
                self.start.next.prev = self.start.prev
                self.start.prev.next = self.start.next
                self.start = self.start.next
    def delete_at_last(self):
        if self.start is not None:
            if self.start == self.start.next:
                self.start = None
            else:
                self.start.prev.prev.next = self.start
                self.start.prev = self.start.prev.prev
    def delete_item(self, data):
        if self.start is not None:
            temp = self.start
            if self.start == self.start.next:
                self.start = None
            elif temp.item == data:
                self.start.next.prev = self.start.prev
                self.start.prev.next = self.start.next
                self.start = self.start.next
            else:
                # temp = self.start
                while temp.next != self.start:
                    if temp.item == data:
                            temp.prev.next = temp.next
                            temp.next.prev = temp.prev
                    temp = temp.next
                if temp.item == data:
                    self.start.prev.prev.next = self.start
                    self.start.prev = self.start.prev.prev
    def __iter__(self):
        return CDLLIterator(self.start)
class CDLLIterator:
    def __init__(self, current):
        self.current = current
        self.start = current
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        if self.current == self.start and self.count == 1:
            raise StopIteration
        else:
            self.count = 1
        data = self.current.item
        self.current = self.current.next
        return data
list = CDLL()
list.insert_at_first(15)
list.insert_at_first(10)
list.insert_at_first(5)
list.insert_at_last(25)
list.insert_after(list.search(15), 20)
list.insert_at_last(30)
list.insert_after(list.search(30), 35)
# list.print()
for i in list:
    print(i, end=' ')
# list.delete_at_first()
# list.delete_at_last()
list.delete_item(35)
list.delete_item(20)
list.delete_item(5)
print()
for i in list:
    print(i, end=' ')