class Book:
    def __init__(self, title, author, year, copies):
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def display_book_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        print(f"Copies: {self.copies}")

    def borrow_book(self):
        if self.copies>0:
            # self.copies = self.copies -1
            self.copies -= 1
            print(f"You have borrowed {self.title} this book")
            print(f"Current Quantity: {self.copies}")
        else:
            print(f"{self.title} book is currently unavailable")


book1 = Book("Python", "IT", "2009", 2)
book1.display_book_info()
book1.borrow_book()
book1.borrow_book()
book1.borrow_book()