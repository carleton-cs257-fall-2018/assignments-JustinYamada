'''
   api_test.py
   Jeff Ondich, 9 May 2012
   Updated for use by Justin Yamada & Justin Hahn in a lab exercise, 16 October 2018
'''

import primechecker
import unittest

class PrimeCheckerTester(unittest.TestCase):
    def setUp(self):
        self.CrimeDataSource = BooksDataSource('Crime.csv')

    def tearDown(self):
        pass

    def test_zero(self):
        self.assertRaises(ValueError, self.prime_checker.is_prime, 0)

    def test_two(self):
        self.assertTrue(self.prime_checker.is_prime(2))

    def test_prime(self):
        self.assertTrue(self.prime_checker.is_prime(97))

    def test_composite(self):
        self.assertFalse(self.prime_checker.is_prime(96))

    def test_primes_below(self):
        self.assertEqual(self.prime_checker.get_primes_below(20), [2, 3, 5, 7, 11, 13, 17, 19])

if __name__ == '__main__':
    unittest.main()
