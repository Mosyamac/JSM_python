class BankAccount:
	def __init__ (self, bonus):
		self.balance = bonus
 
	def deposit (self, amount):
		self.balance += amount
 
	def withdraw (self, amount):
		if self.balance > amount:
			self.balance -= amount
		else:
			self.balance = 0
 
	def interest (self, rate):
		self.balance = self.balance + (self.balance * rate)/100
 
	def get(self):
		return self.balance
 
if __name__ == '__main__':
	account = BankAccount(30)
	account.deposit(50)
	account.withdraw(10)
	account.interest(8.5)
	balance = account.get()
	print balance
