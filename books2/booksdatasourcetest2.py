'''
   booksdatasourcetest.py
   Justin Hahn, Justin Yamada 20 September 2018
'''


import unittest

class booksDataSourceTest(unittest.TestCase):
    def setUp(self):
        self.booksDataSourceTest = booksdatasource.BooksDataSource('bookstest.csv','authorstest.csv', 'books_authorstest.csv')

    def tearDown(self):
        pass

    def test_book(self):
        self.assertEqual(booksdatasource.book(5), {'id': 5, 'title': 'Book Five', 'publication_year': 1005})

    def test_books__show_all_books(self):
        self.assertEqual(booksdatasource.books(),
        {'id': 0, 'title': 'Book Zero', 'publication_year': 1000},
        {'id': 1, 'title': 'Book One', 'publication_year': 1001},
        {'id': 2, 'title': 'Book Two', 'publication_year': 1002},
        {'id': 3, 'title': 'Book Three', 'publication_year': 1003},
        {'id': 4, 'title': 'Book Four', 'publication_year': 1004},
        {'id': 5, 'title': 'Book Five', 'publication_year': 1005},
        {'id': 6, 'title': 'Book Double', 'publication_year': 1000},
        {'id': 7, 'title': 'Book Single One', 'publication_year': 1000},
        {'id': 8, 'title': 'Book Single Two', 'publication_year': 1000})

    def test_books_only_id(self):
        self.assertEqual(booksdatasource.books(author_id=3),
        {'id': 3, 'title': 'Book Three', 'publication_year': 1003})

    def test_books_with_start_year_end_year_sorted_by_title(self):
        self.assertEqual(booksdatasource.book(author_id=None, search_text=None, start_year=1000, end_year=1002, sort_by='title'),
        {'id': 1, 'title': 'Book One', 'publication_year': 1001},
        {'id': 7, 'title': 'Book Single One', 'publication_year': 1000},
        {'id': 8, 'title': 'Book Single Two', 'publication_year': 1000},
        {'id': 2, 'title': 'Book Two', 'publication_year': 1002},
        {'id': 0, 'title': 'Book Zero', 'publication_year': 1000})

    def test_books_with_start_year_end_year_sorted_by_publication_year(self):
        self.assertEqual(booksdatasource.book(author_id=None, search_text=None, start_year=1000, end_year=1002, sort_by='year'),
        {'id': 7, 'title': 'Book Single One', 'publication_year': 1000},
        {'id': 8, 'title': 'Book Single Two', 'publication_year': 1000},
        {'id': 0, 'title': 'Book Zero', 'publication_year': 1000},
        {'id': 1, 'title': 'Book One', 'publication_year': 1001},
        {'id': 2, 'title': 'Book Two', 'publication_year': 1002})

    def test_author(self):
        self.assertEqual(booksdatasource.author(3),
        {'id': 3, 'last_name': 'Three', 'first_name': 'Delta', 'birth_year': 200, 'death_year': 1003})

    def test_authors_show_all_authors(self):
        self.assertEqual(booksdatasource.authors(),
        {'id': 0, 'last_name': 'Zero', 'first_name': 'Alpha', 'birth_year': 50, 'death_year': 1000},
        {'id': 1, 'last_name': 'One', 'first_name': 'Bravo', 'birth_year': 100, 'death_year': 1001},
        {'id': 2, 'last_name': 'Two', 'first_name': 'Charlie', 'birth_year': 150, 'death_year': 1002},
        {'id': 3, 'last_name': 'Three', 'first_name': 'Delta', 'birth_year': 200, 'death_year': 1003},
        {'id': 4, 'last_name': 'Four', 'first_name': 'Echo', 'birth_year': 250, 'death_year': 1004},
        {'id': 5, 'last_name': 'Five', 'first_name': 'Foxtrot', 'birth_year': 300, 'death_year': 1005},
        {'id': 6, 'last_name': 'One', 'first_name': 'Double', 'birth_year': 950, 'death_year': 1000},
        {'id': 7, 'last_name': 'Two', 'first_name': 'Double', 'birth_year': 950, 'death_year': 1000},
        {'id': 7, 'last_name': 'Only', 'first_name': 'Single', 'birth_year': 950, 'death_year': 1000})

    def test_authors_only_id(self):
        self.assertEqual(booksdatasource.authors(book_id=0),
        {'id': 0, 'last_name': 'Zero', 'first_name': 'Alpha', 'birth_year': 50, 'death_year': 1000})

    def test_authors_with_start_year_end_year_sorted_by_birth_year(self):
        self.assertEqual(booksdatasource.authors(book_id=None, search_text=None,start_year=51, end_year=300, sort_by='birth_year'),
        {'id': 1, 'last_name': 'One', 'first_name': 'Bravo', 'birth_year': 100, 'death_year': 1001},
        {'id': 2, 'last_name': 'Two', 'first_name': 'Charlie', 'birth_year': 150, 'death_year': 1002},
        {'id': 3, 'last_name': 'Three', 'first_name': 'Delta', 'birth_year': 200, 'death_year': 1003},
        {'id': 4, 'last_name': 'Four', 'first_name': 'Echo', 'birth_year': 250, 'death_year': 1004},
        {'id': 5, 'last_name': 'Five', 'first_name': 'Foxtrot', 'birth_year': 300, 'death_year': 1005})

    def test_authors_with_start_year_end_year_sorted_by_last_name(self):
        self.assertEqual(booksdatasource.authors(book_id=None, search_text=None,start_year=51, end_year=300, sort_by='last_name'),
        {'id': 5, 'last_name': 'Five', 'first_name': 'Foxtrot', 'birth_year': 300, 'death_year': 1005},
        {'id': 1, 'last_name': 'One', 'first_name': 'Bravo', 'birth_year': 100, 'death_year': 1001},
        {'id': 2, 'last_name': 'Two', 'first_name': 'Charlie', 'birth_year': 150, 'death_year': 1002},
        {'id': 3, 'last_name': 'Three', 'first_name': 'Delta', 'birth_year': 200, 'death_year': 1003},
        {'id': 4, 'last_name': 'Four', 'first_name': 'Echo', 'birth_year': 250, 'death_year': 1004})

    def test_books_for_author_of_single_book(self):
        self.assertEqual(booksdatasource.books_for_author(1),
        {'id': 1, 'title': Book One, 'publication year': 1001})

    def test_books_for_author_of_multiple_books(self):
        self.assertEqual(booksdatasource.books_for_author(8),
        {'id': 7, 'title': Book Single One, 'publication year': 1000},
        {'id': 8, 'title': Book Single Two, 'publication year': 1000})

    def test_authors_for_book_with_single_author(self):
        self.assertEqual(booksdatasource.authors_for_book(4),
        {'id': 4, 'last_name': Four, 'first_name': Echo, 'birth_year': 250, 'death_year': 1004})

    def test_authors_for_book_with_multiple_authors(self):
        self.assertEqual(booksdatasource.authors_for_book(6),
        {'id': 6, 'last_name': One, 'first_name': Double, 'birth_year': 950, 'death_year': 1000},
        {'id': 7, 'last_name': Two, 'first_name': Double, 'birth_year': 950, 'death_year': 1000})

    def test_wrong_author_id(self):
        self.assertRaises(ValueError, self.data_source.books,author_id=-1)

if __name__ == '__main__':
    unittest.main()
