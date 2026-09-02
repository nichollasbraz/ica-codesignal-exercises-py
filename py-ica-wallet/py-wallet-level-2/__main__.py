from classes import *

c1 = Wallet()
print(c1.create_account("Malagoli", 10))
print(c1.deposit("Malagoli", 10, 300))
print(c1.withdraw("Malagoli", 10, 100))
print(c1.create_account("Renato", 11))
print(c1.transfer("Malagoli", "Renato", 15, 98))
print(c1.transfer("Malagoli", "Renato", 16, 300))
print(c1.transfer("Nogueira", "Malagoli", 29, 20))
print(c1.transfer("Renato", "Malagoli", 30, 90))
print(c1.total_spent)
