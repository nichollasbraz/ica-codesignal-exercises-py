from classes import *

c = CreditCard()

print(c.create_card("tst", 0, 2000))
print(c.get_available_balance("tst"))
print(c.make_purchase("tst", 15, 950, "ses"))
print(c.get_card_balance("tst"))
print(c.make_purchase("tst", 20, 120, "sos"))
print(c.get_card_balance("tst"))
print(c.top_spending_categories("tst", 2))
print(c.get_purchase_history("tst"))
print(c.create_invoice("tst", 0, 30))
