class Book: #Stores book attributes
    def __init__(self, ID, name, author, genre, price, stock):
        self.ID = ID
        self.name = name
        self.author = author
        self.genre = genre
        self.price = price
        self.stock = stock

    def show(self):
        print(self.ID, self.name, self.author, self.genre, self.price)

    def book_string(self):
        print(str(self.ID) + " " + str(self.name) + " " + str(self.author) + " " + str(self.genre) + " " + str(self.price))

    def get_id(self):
        return(self.ID)

    def get_name(self):
        return(self.name)

    def get_author(self):
        return(self.author)

    def get_genre(self):
        return(self.genre)

    def get_price(self):
        return(self.price)

    def get_stock(self):
        return (self.stock)

class bookDatabase: #Stores all books
    def __init__(self):
        self.books = dict()

    def add_book(self, Book):
        self.books[Book.ID] = Book

    def remove_book(self, Book):
        del self.books[Book.ID]

    def get_book(self, ID):
        return self.books[ID]

    def show_All(self):
        for Book in self.books.values():
            Book.show()

    def book_list(self):
        return self.books.values()

class bookSearch(bookDatabase): #searches for book
    def __init__(self, books):
        self.books = books

    def search_book(self, search, books):
        for Book in books:
            if (search == Book.name):
                print(Book.name + " has been found!")
                break
            else:
                print("Searching...not found")

class bookInventory(bookDatabase): #prints all book titles and stock count
    def __init__(self, books):
        self.books = books

    def showInventory(self, books):
        print("---Current Book Inventory---")
        for Book in books:
            print(f'{Book.ID}' + " " + Book.name + " (" + f'{Book.stock}' + " in stock)")


if __name__ == "__main__":
    data = bookDatabase()
    search = ""
    book1 = Book(1, "Harry Potter", "J.K Rowling", "Fantasy", 17.99, 6)
    book2 = Book(2, "The Ministry of Time", "Kaliane Bradley", "Romance", 14.99, 3)
    book3 = Book(3, "The Demon of Unrest", "Erik Larson", "Biography", 19.99, 5)
    book4 = Book(4, "Real Americans", "Rachel Khong", "Urban Fiction", 20.99, 2)
    book5 = Book(5, "Skin & Bones", "Renee Wilson", "Mystery", 24.99, 8)

    data.add_book(book1)
    data.add_book(book2)
    data.add_book(book3)
    data.add_book(book4)
    data.add_book(book5)

    #data.show_All()
    #bookToSearch = bookSearch(data)
    #bookToSearch.search_book("The Demon of Unrest", data.book_list())
    #bookStock = bookInventory(data)
    #bookStock.showInventory(data.book_list())

