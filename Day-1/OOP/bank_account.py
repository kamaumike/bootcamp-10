class Bank_Account(object):
	"Bank Account Class"

	def __init__(self,balance):
		self.balance = balance

	def deposit(self,deposit_amount):
		self.balance += deposit_amount
		return self.balance
    
	def withdraw(self,withdraw_amount):
		if withdraw_amount > self.balance:
			return self.balance
		else:
			self.balance -= withdraw_amount
			return self.balance


class Savings_Account(Bank_Account):
	"""Savings Account Class"""

	def balance_after_interest_earned(self, interest_earned):
		self.interest_earned = interest_earned
		return super(Savings_Account,self).deposit(interest_earned)

