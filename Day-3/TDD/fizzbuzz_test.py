import unittest
from fizzbuzz import fizzbuzz

class FizzbuzzTest(unittest.TestCase):
	def test_multiples_of_15(self):
		self.assertEqual(fizzbuzz(30), 'FizzBuzz')

	def test_multiples_of_5(self):
		self.assertEqual(fizzbuzz(25), 'Buzz')

	def test_multiples_of_3(self):
		self.assertEqual(fizzbuzz(12), 'Fizz')

	def test_for_non_multiples(self):
		self.assertEqual(fizzbuzz(17), 17)

	def test_for_non_integer(self):
		self.assertEqual(isinstance(fizzbuzz(0), int), 0)

if __name__ == '__main__':
	unittest.main()
