import unittest
from factorial import factorial

class FactorialTest(unittest.TestCase):
	
	def test_input_is_an_integer(self):
		self.assertEqual(isinstance(factorial(6), int), True, msg="Should be an 'int'")

	def test_if_factorial_zero_is_one(self):
		self.assertEqual(factorial(0), 1, msg="Expect to return 1")

	def test_if_factorial_one_is_one(self):
		self.assertEqual(factorial(1), 1, msg="Field cannot be empty!")

	def test_if_output_is_correct(self):
		self.assertEqual(factorial(6), 720, msg="The output is expected is 720")

if __name__ == '__main__':
	unittest.main()