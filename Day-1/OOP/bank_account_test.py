import unittest

from bank_account import Bank_Account, Savings_Account

class BankAccountClassTest(unittest.TestCase):
    """Tests for the Bank_Account class and Savings_Account class"""

    def test_bank_account_instance(self):
        my_account = Bank_Account(32000)
        self.assertIsInstance(my_account, Bank_Account, msg="The object should be an instance of the `Bank_Account` class")

    def test_amount_deposited(self):
    	my_account = Bank_Account(32000)
    	self.assertEqual(my_account.deposit(5000), 37000, msg="Expected 37000")

    def test_amount_withdrawn_is_less_than_balance(self):
    	my_account = Bank_Account(32000)
    	self.assertEqual(my_account.withdraw(2000), 30000, msg="Expected 30000 balance")

    def test_amount_withdrawn_is_greater_than_balance(self):
    	my_account = Bank_Account(32000)
    	self.assertEqual(my_account.withdraw(32001), 32000 , msg="Insufficient funds!")

    def test_savings_account_instance(self):
        my_account = Savings_Account(32000)
        self.assertIsInstance(my_account, Savings_Account, msg="The object should be an instance of the `Savings_Account` class")

    def test_balance_after_interest_earned(self):
    	my_account = Savings_Account(32000)
    	self.assertEqual(my_account.balance_after_interest_earned(3000), 35000, msg="Expected 35000 balance")

if __name__ == '__main__':
    unittest.main()

