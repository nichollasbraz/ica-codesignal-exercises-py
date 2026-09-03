from classes import *

c1 = Wallet()
print(c1.create_account("Malagoli", 29))
print(c1.accounts)
print(c1.deposit("Malagoli", 29, 200))
print(c1.accounts)
print(c1.withdraw("Malagoli", 29, 140))
print(c1.accounts)
