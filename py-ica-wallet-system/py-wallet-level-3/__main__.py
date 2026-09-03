from classes import *

c1 = Wallet()
print(c1.create_account("Malagoli", 0))
print(c1.deposit("Malagoli", 0, 300))
print(c1.pay_with_cashback("Malagoli", 20, 150, 10))
print(c1.pay_with_cashback("Malagoli", 30, 150, 10))
print(c1.__dict__)
print(c1.top_spenders(15, 1))
print(c1.get_payment_status("Malagoli", 300, "payment1"))
