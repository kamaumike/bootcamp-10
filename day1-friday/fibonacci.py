#prints a list of fibonnaci numbers
def fibonacci(number):
	"""Generate Fibonacci sequence"""
	
	mylist = [0,1];

	for i in range(2,number):
		mylist.append(mylist[i-1] + mylist[i-2]);
		
	print("Your Fibonacci numbers are" , mylist)
	
fibonacci(10)