class Node:
    def __init__(self,prev=None,item=None, next=None):
        self.prev = prev
        self.next = next
        self.item =item
class DLL:
    def __init__(self, start=None):
        self.start = start
    def is_empty(self):
        return self.start is None
    def insert_at_start(self, data):
        n = Node(None, data, self.start)
        if self.start is not None:
            self.start.prev = n
        self.start = n
    def insert_at_last(self, data):
        n = Node(None, data, None)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
            n.prev = temp
        else:
            self.start = n
    def search(self, data):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    return temp
                temp = temp.next
        return None
    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(temp, data, temp.next)
            temp.next = n
            if n.next:
                n.next.prev = n
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next
    def delete_at_start(self):
        if self.start is not None:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None
        else:
            print("List is empty")
    def delete_at_last(self):
        if self.start is None:
            print("List is empty")
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
    def delete_item(self, data):
        if self.start is None:
            print("List is empty")
        elif self.start.next is None:
            if self.start.item == data:
                self.start = None
            else:
                print(f"{data} is not present in the list")
        else:
            temp = self.start
            if temp.item == data:
                self.start = temp.next
            else:
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next
    def __iter__(self):
        return DLLIterator(self.start)
class DLLIterator:
    def __init__(self, current):
        self.current = current
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data