class Book:
    def __init__(self, book_name,author):
        self.book_name=book_name
        self.author=author
        self.status =True ##ספר זמין
        self.borrow_name = None
    def book_borrowed(self,user_name):
        if not self.status:
            print("The book is already borrowed")
            return False
        self.status=False #הספר אינו זמין עכשיו#
        self.borrow_name=user_name
        return True
    def book_returned(self):
        if self.status:##הספר זמין להשאלה
            print("The book is available")
            return False
        self.status = True
        self.borrow_name =None
        return True
    def print_details(self):
        print( f"'{self.book_name}' by {self.author}")

class Reader:
    def __init__(self,user_id,user_name):
        self.user_id=user_id
        self.user_name=user_name
        self.borrowed_books = []
        self.limit= 3## מגבלת הקורא היא עד 3 ספרים

    def borrow_book(self,book):
        if len(self.borrowed_books) >= self.limit:
            print("Your borrowing limit is over (3 books).")
            return False
        if book.book_borrowed(self.user_name):
            self.borrowed_books.append(book)
            print(f"Successfully borrowed {book.book_name}")
            return True
        else:
            print("The book isn't available.")
            return False

    def return_book(self,book):
        for i in self.borrowed_books:
            if i ==book:
                book.book_returned()
                self.borrowed_books.remove(book)
                print(f"Returned {book.book_name}")
                return True
        print("The book isnt in your list")
        return  False

    def print_details(self):
        print(f"User Name: {self.user_name}, ID: {self.user_id}")
        print("Borrowed Books List:")
        for book in self.borrowed_books:
            print(book.print_details())

class Librarian(Reader):
    def __init__(self,user_id,user_name):
        super().__init__(user_id,user_name)
        self.num_readers=[]
        self.limit= 5## מגבלת הספרן היא עד 5 ספרים

    def print_details(self):
        print(f"User Name: {self.user_name} \nID: {self.user_id}")
        print("Readers managed by librarian:")
        for reader in self.num_readers:
            print(f"Reader ID: {reader.user_id}, Name: {reader.user_name}")

    def add_new_reader(self,reader):
        self.num_readers.append(reader)

class ChiefLibrarian(Librarian):
    def __init__(self,user_id,user_name):
        super().__init__(user_id,user_name)
        self.librarians_list=[]
        self.limit= 7## מגבלת המנהל היא עד 7 ספרים

    def print_details(self):
        print(f"Name: {self.user_name} \nID: {self.user_id}")
        print("Librarians under responsibility:")
        for lib in self.librarians_list:
            print(f"Librarians ID: {lib.user_id}, Name: {lib.user_name}")

    def add_new_librarian(self,lib):
        self.librarians_list.append(lib)

def main():
    # Books
    b1 = Book("Harry Potter", "J.K. Rowling")
    b2 = Book("The Hobbit", "J.R.R. Tolkien")
    b3 = Book("Dune", "Frank Herbert")

    # Reader tests
    r1 = Reader("101", "Dan")
    r1.print_details()

    r2 = Reader("102", "Maya")
    r2.borrow_book(b1)
    r2.print_details()

    r3 = Reader("103", "Yosef")
    r3.borrow_book(b2)
    r3.borrow_book(b3)
    r3.print_details()

    # Librarian tests
    l1 = Librarian("200", "Sarah")
    l1.print_details()

    l2 = Librarian("201", "David")
    l2.add_new_reader(r1)
    l2.add_new_reader(r2)
    l2.print_details()

    # Chief Librarian tests
    c1 = ChiefLibrarian("300", "Noa")
    c1.print_details()

    c2 = ChiefLibrarian("301", "Adam")
    c2.add_new_librarian(l1)
    c2.add_new_librarian(l2)
    c2.print_details()
main()