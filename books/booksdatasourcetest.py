'''
   booksdatasourcetest.py
   Justin Hahn, Justin Yamada 20 September 2018
'''


import unittest

class booksDataSourceTest(unittest.TestCase):
    def setUp(self):
        self.booksDataSourceTest = primechecker.PrimeChecker(100)

    def tearDown(self):
        pass

    def test_zero(self):
        self.assertRaises(ValueError, self.prime_checker.is_prime, 0)

    def test_two(self):
        self.assertTrue(self.prime_checker.is_prime(2))

    def test_three(self):
        self.assertTrue(self.prime_checker.is_prime(97))

    def test_composite(self):
        self.assertFalse(self.prime_checker.is_prime(96))

    def test_primes_below(self):
        self.assertEqual(self.prime_checker.get_primes_below(20), [2, 3, 5, 7, 11, 13, 17, 19])

if __name__ == '__main__':
    unittest.main()
