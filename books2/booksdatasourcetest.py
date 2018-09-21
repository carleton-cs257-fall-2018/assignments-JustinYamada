'''
   booksdatasourcetest.py
   Justin Hahn, Justin Yamada 20 September 2018
'''


import unittest

class booksDataSourceTest(unittest.TestCase):
    def setUp(self):
        self.booksDataSourceTest = booksdatasource.BooksDataSource('books.csv','authors.csv', 'books_authors_link.csv')

    def tearDown(self):
        pass

    def test_book(self):
        self.assertEqual(booksdatasource.book(5), "Book Five")

    def test_author(self):
        self.assertEqual(booksdatasource.author(3), "Charlie Author Three")

    def test_authors_return_all_authors(self)
        self.assertEqual(booksdatasource.authors(), [Alpha Author One, Bravo Author Two, Charlie Author Three, Delta Author Four, Echo Author Five])

    def test_composite(self):
        self.assertFalse(self.prime_checker.is_prime(96))

    def test_primes_below(self):
        self.assertEqual(self.prime_checker.get_primes_below(20), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_wrong_author_id(self):
        self.assertRaises(ValueError, self.data_source.books,author_id=-1)

if __name__ == '__main__':
    unittest.main()
