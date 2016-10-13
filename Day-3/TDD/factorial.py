def factorial(digit):
	'''Returns the factorial of a number'''	
	result = 1	
	for i in range(2, digit+1):
		result *= i
	return	result

		