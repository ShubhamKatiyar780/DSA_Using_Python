class Node:
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next
class CLL:
    def __init__(self, last = None):
        self.last = last
    def is_empty(self):
        return self.last is None
    def insert_at_first(self, data):
        n = Node(data)
        if self.is_empty():
            self.last = n
            n.next = n
        else:
            n.next = self.last.next
            self.last.next = n
    def insert_at_last(self, data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
            self.last = n
    def search(self, data):
        if self.is_empty():
            return None
        temp = self.last.next
        while temp != self.last:
            if temp.item == data:
                return temp
            temp = temp.next
        if temp.item == data:
            return temp
        return None        
    def insert_after(self, temp, data):
        if temp is not None :
            n = Node(data, temp.next)
            temp.next = n
            if temp == self.last:
                self.last = n
    def print(self):
        if not self.is_empty():
            temp = self.last.next
            while temp != self.last:
                print(temp.item, end=' ')
                temp = temp.next
            print(temp.item)
    def delete_at_start(self):
        if not self.is_empty():
            if self.last == self.last.next:
                self.last = None
            else:
                self.last.next = self.last.next.next
    def delete_at_last(self):
        if not self.is_empty():
            if self.last == self.last.next:
                self.last = None
            else:
                temp = self.last.next
                while temp.next != self.last:
                    temp = temp.next
                temp.next = self.last.next
                self.last = temp
    def delete_item(self, data):
        if not self.is_empty():
            if self.last == self.last.next:
                if self.last.item == data:
                    self.last = None
            else:
                if self.last.next.item == data:
                    self.last.next = self.last.next.next
                else:
                    temp = self.last.next
                    while temp != self.last:
                        if temp.next == self.last:
                            if temp.next.item == data:
                                temp.next = self.last.next
                                self.last = temp
                            break
                        if temp.next.item == data:
                            temp.next = temp.next.next
                            break
                        temp = temp.next
list = CLL()
list.insert_at_first(20)
list.insert_at_first(10)
list.insert_at_last(40)
list.insert_after(list.search(20), 30)
list.insert_after(list.search(40), 50)
list.print()
list.delete_at_start()
list.delete_at_last()
list.delete_item(30)
list.print()