class Book:
    def __init__(self, bookid, title, price):
        self.bookid = bookid
        self.title = title
        self.price = price
    def show(self):
        print(f"Book Id: {self.bookid}, Book Title: {self.title}, Book Price: {self.price}")
obj = Book(1232, 'Mathematics', 450)
obj.show()