import unittest
from mock import patch
from io import StringIO
from main import *

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book1 = Book(1, "Harry Potter", "J.K Rowling", "Fantasy", 17.99, 6)

    def test_book_attributes(self):
        self.assertEqual(self.book1.ID, 1)
        self.assertEqual(self.book1.name, "Harry Potter")
        self.assertEqual(self.book1.author, "J.K Rowling")
        self.assertEqual(self.book1.genre, "Fantasy")
        self.assertEqual(self.book1.price, 17.99)
        self.assertEqual(self.book1.stock, 6)

    def test_book_methods(self):
        self.assertEqual(self.book1.get_id(), 1)
        self.assertEqual(self.book1.get_name(), "Harry Potter")
        self.assertEqual(self.book1.get_author(), "J.K Rowling")
        self.assertEqual(self.book1.get_genre(), "Fantasy")
        self.assertEqual(self.book1.get_price(), 17.99)
        self.assertEqual(self.book1.get_stock(), 6)

class TestBookDatabase(unittest.TestCase):
    def setUp(self):
        self.data = bookDatabase()
        self.book1 = Book(1, "Harry Potter", "J.K Rowling", "Fantasy", 17.99, 6)

    def test_add_book(self):
        self.data.add_book(self.book1)
        self.assertEqual(len(self.data.books), 1)

    def test_remove_book(self):
        self.data.add_book(self.book1)
        self.data.remove_book(self.book1)
        self.assertEqual(len(self.data.books), 0)

    def test_get_book(self):
        self.data.add_book(self.book1)
        self.assertEqual(self.data.get_book(1), self.book1)

    def test_show_all(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.data.add_book(self.book1)
            self.data.show_All()
            self.assertEqual(fake_out.getvalue().strip(), "1 | Harry Potter | J.K Rowling | Fantasy | 17.99")

class TestBookSearch(unittest.TestCase):
    def setUp(self):
        self.data = bookDatabase()
        self.book1 = Book(1, "Harry Potter", "J.K Rowling", "Fantasy", 17.99, 6)
        self.data.add_book(self.book1)
        self.book_search = bookSearch(self.data)

    @patch('sys.stdout', new_callable=StringIO)
    def test_search_book_found(self, mock_stdout):
        self.book_search.search_book("Harry Potter", self.data.book_list())
        self.assertEqual(mock_stdout.getvalue().strip(), "Harry Potter has been found!")

    @patch('sys.stdout', new_callable=StringIO)
    def test_search_book_not_found(self, mock_stdout):
        self.book_search.search_book("Non-existent Book", self.data.book_list())
        self.assertEqual(mock_stdout.getvalue().strip(), "Searching...not found")

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.data = bookDatabase()
        self.book1 = Book(1, "Harry Potter", "J.K Rowling", "Fantasy", 17.99, 6)
        self.data.add_book(self.book1)
        self.cart = shoppingCart(self.data.book_list())

    @patch('builtins.input', side_effect=[1])
    def test_add_to_cart(self, mock_input):
        self.cart.addToCart()
        self.assertEqual(len(self.cart.items), 1)

    @patch('builtins.input', side_effect=[0,1])
    def test_remove_from_cart(self, mock_input):
        self.cart.addToCart()
        self.cart.removeFromCart()
        self.assertEqual(len(self.cart.items), 0)

    def test_price_cart(self):
        self.cart.addToCart()
        self.assertEqual(self.cart.priceCart(), 18.71)

if __name__ == '__main__':
    unittest.main()
