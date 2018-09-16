# test.py
# Written by Justin Hahn
#
# Meant to Test books1.py
#
import unittest
import books1

class testParse(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(len(books1.getBooks([])), 0)

if __name__ == "__main__":
    unittest.main() # run all tests
