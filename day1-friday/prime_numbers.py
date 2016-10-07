def prime_number(num):	
	"""Generate prime nummbers"""
		
	for i in range(2,num + 1):
		prime = True
		for j in range(2,i):
			if i % j == 0:
				prime = False
		if prime: 
			print(i)		

prime_number(10)

