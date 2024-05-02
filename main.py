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

class shoppingCart(bookDatabase): #stores items and conducts item manipulation in the cart
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
        taxPrice = price + (price*0.04)
        return round(taxPrice,2)

    def showCart(self):
        print("--- Cart Items ---")
        for item in self.items:
            currentIndex = self.items.index(item)
            print(currentIndex, item.name, item.price)
        print("")

def printInstructions(): #prints instructions
    print("Type C to view cart items")
    print("Type R to remove an item from cart")
    print("Type S to search for a book")
    print("Type I to check inventory")
    print("Type A to start adding items to the cart")
    print("Type P to get total cart price")
    print("Type X to exit")
    print("Type F to checkout")

def printReceipt(shoppingCart):
    print("Customer: " + username)
    print(shoppingCart.showCart())

def checkout(shoppingCart):
    totalPrice = shoppingCart.priceCart()
    print("Items added to cart. Your total is " + f'{totalPrice}')
    print("Would you like in-person pickup (1) or delivery (2)?")
    userDelivery = int(input())
    if(userDelivery == 1):
        print("In-Person Pickup Selected.")
    elif(userDelivery == 2):
        print("Delivery Selected.")

    print("Confirm purchase? (Y/N): ")
    userCheckout = (input())
    if (userCheckout == "Y"):
        print("Order confirmed. Prnting receipt...")
        printReceipt(shoppingCart)
    elif (userCheckout == "N"):
        print("Order cancelled.")
    global done
    done = True

def inputHandler(in_var, cart): #handles user input for commands while the main program loop is running
    char_inputs = ["C", "A", "S", "I" "R", "P", "F", "X"]
    if(in_var == "C"):
        cart.showCart() #shows current cart
    if(in_var == "R"):
        cart.removeFromCart() #removes item from cart
    if(in_var == "S"):
        print("Book search started")
        bookToSearch = bookSearch(data)
        print("Enter a title: ")
        userSearch = input()
        bookToSearch.search_book(userSearch, data.book_list()) #user book search
        print("Exiting book search...")
    if(in_var == "A"):
        shoppingCart.addToCart(cart) #adds item to cart
    if(in_var == "I"):
        print("Looking through inventory...")
        bookStock = bookInventory(data)
        bookStock.showInventory(data.book_list()) #shows stock of all books in database
        print("Exiting inventory...")
    if(in_var == "P"):
        print("Total: $" + f'{cart.priceCart()}') #gets total price of items in cart
    if(in_var == "F"):
        print("Wrapping up...") #compiles and outputs a receipt
        checkout(cart)
    if(in_var=="X"):
        global done
        done = True
        print("Thank you! Application closing...") #exits the application
    #if in_var not in char_inputs:
    #    print("Incorrect input!")

if __name__ == "__main__": #main
    data = bookDatabase()
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

    print("Thank you for shopping! Exiting appilcation...")
