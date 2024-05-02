done = False
class Book: #Stores book attributes
    def __init__(self, ID, name, author, genre, price, stock):
        self.ID = ID
        self.name = name
        self.author = author
        self.genre = genre
        self.price = price
        self.stock = stock

    def show(self):
        print(str(self.ID) + " | " + str(self.name) + " | " + str(self.author) + " | " + str(self.genre) + " | " + str(self.price))

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

class shoppingCart(bookDatabase):
    def __init__(self, books):
        self.items = []
        self.books = books

    def addToCart(self):
        print("Enter a book ID to add: ")
        bookID = int(input())
        books = self.books
        for Book in books:
            if (bookID == Book.ID):
                self.items.append(Book)
                print(Book.name + " added to cart!")
                break
            else:
                print("Book ID not found. Exiting...")

    def removeFromCart(self):
         print("Enter a book index to remove: ")
         bookIndex = int(input())
         books = self.books
         for Book in books:
            if (bookIndex == (Book.ID - 1)):
                self.items.pop(bookIndex)
                print(Book.name + " removed from cart!")
                break
            else:
                print("Book ID not found. Exiting...")

    def priceCart(self):
        price = 0
        for item in self.items:
            price = price+item.price
        return price

    def showCart(self):
        print("--- Cart Items ---")
        for item in self.items:
            currentIndex = self.items.index(item)
            print(currentIndex, item.name, item.price)
        print("")

def printInstructions():
    print("Type C to view cart items")
    print("Type R to remove an item from cart")
    print("Type S to search for a book")
    print("Type I to check inventory")
    print("Type A to start adding items to the cart")
    print("Type P to get total cart price")
    print("Type X to exit")
    print("Type F to checkout")



def inputHandler(in_var, cart):
    char_inputs = ["C", "A", "S", "I" "R", "P", "F", "X"]
    if(in_var == "C"):
        cart.showCart()
    if(in_var == "R"):
        cart.removeFromCart()
    if(in_var == "S"):
        print("Book search started")
        bookToSearch = bookSearch(data)
        print("Enter a title: ")
        userSearch = input()
        bookToSearch.search_book(userSearch, data.book_list())
        print("Exiting book search...")
    if(in_var == "A"):
        shoppingCart.addToCart(cart)
    if(in_var == "I"):
        print("Looking through inventory...")
        bookStock = bookInventory(data)
        bookStock.showInventory(data.book_list())
        print("Exiting inventory...")
    if(in_var == "P"):
        print("Total: $" + f'{cart.priceCart()}')
    if(in_var == "F"):
        print("FInish.")
    if(in_var=="X"):
        global done
        done = True
        print("Thank you! Application closing...")
    #if in_var not in char_inputs:
    #    print("Incorrect input!")

if __name__ == "__main__":
    data = bookDatabase()
    #search = ""
    username = ""
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

    print("Welcome. Please enter your username: ")
    username = input()
    print("You have successfully logged in, " + username + ". Here are our selection of books: ")
    cart = shoppingCart(data.book_list())
    printInstructions()

    while(done == False):
        data.show_All()
        print("Type a command: ")
        input_var = input()
        inputHandler(input_var, cart)


    #data.show_All()
    #bookToSearch = bookSearch(data)
    #bookToSearch.search_book("The Demon of Unrest", data.book_list())
    #bookStock = bookInventory(data)
    #bookStock.showInventory(data.book_list())

