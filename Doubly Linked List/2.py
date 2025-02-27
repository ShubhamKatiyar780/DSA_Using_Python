class Node:
    def __init__(self, item = None, prev = None, next = None):
        self.item = item
        self.prev = prev
        self.next = next
class DLL:
    def __init__(self, start = None):
        self.start = start
    def __iter__(self):
        return DLLIterator(self.start)
    def is_empty(self):
        return self.start == None
    def insert_at_start(self, data):
        n = Node(data, None, self.start)
        if not self.is_empty():
            self.start.prev = n
        self.start = n
    def insert_at_last(self, data):
        n = Node(data, None, None)
        temp = self.start
        if not self.is_empty():
            while temp.next is not None:
                temp = temp.next
            temp.next = n
            n.prev = temp
        else:
            self.start = n
    def search(self, data):
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                if temp.item == data:
                    return temp
                temp = temp.next
            if temp.item == data:
                return temp
        return None
    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(data, temp, temp.next)
            temp.next = n
            if n.next is not None:
                n.next.prev = n
    def print(self):
        temp = self.start
        if temp is not None:
            while temp.next is not None:
                print(temp.item,end=' ')
                temp = temp.next
            print(temp.item)
    def delete_at_start(self):
        if self.start is not None:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None
    def delete_at_last(self):
        if self.start is not None:
            temp =self.start
            if temp.next is None:
                self.start = None
            else:
                # while temp.next is not None:
                #     temp = temp.next
                # temp.prev.next.next = None
#-----------------------OR-------------------------               
                while temp.next.next is not None:
                    temp = temp.next
                temp.next = None
    def delete_item(self, data):
        if self.start is not None:
            if self.start.next is None:
                if self.start.item == data:
                    self.start = None
            else:
                temp = self.start
                if temp.item == data:
                    temp.next.prev = None
                    self.start = temp.next
                else:
                    while temp.next is not None:
                        if temp.item == data:
                            temp.next.prev = temp.prev
                            temp.prev.next = temp.next
                        temp = temp.next
                    if temp.item == data:
                        temp.prev.next = None
class DLLIterator:
    def __init__(self, current):
        self.current = current
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data
list = DLL()
list.insert_at_start(20)
list.insert_at_start(10)
list.insert_at_last(40)
list.insert_after(list.search(20), 30)
list.insert_after(list.search(20), 30)
list.insert_after(list.search(20), 30)
list.insert_after(list.search(20), 30)
list.insert_at_start(5)
list.insert_after(list.search(5), 7)
list.print()
# list.delete_at_start()
# list.delete_at_last()
list.delete_item(30)
for i in list:
    print(i, end=' ')