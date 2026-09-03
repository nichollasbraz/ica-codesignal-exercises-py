class CreditCard():
    def __init__(self):
        self.accounts = {}
        self.purchases = {}


    def create_card(self, card_id: str, timestamp: int, credit_limit: int) -> bool:
        if card_id in self.accounts:
            return False

        self.accounts[card_id] = {
            "limit": credit_limit,
            "amount_used": 0,
            "total_purchases": len(self.purchases)
        }
        self.purchases[card_id] = []
        return True


    def get_available_balance(self, card_id: str) -> int | None:
        if card_id not in self.accounts:
            return None
        else:
            available = self.accounts[card_id]["limit"] - self.accounts[card_id]["amount_used"]
            return available


    def make_purchase(self, card_id: str, timestamp: int, amount: int, category: str) -> bool:
        if card_id not in self.accounts:
            return False
        available = self.accounts[card_id]["limit"] - self.accounts[card_id]["amount_used"]
        if amount > available:
            return False

        self.accounts[card_id]["amount_used"] += amount    

        new_purchase = {
            "category": category,
            "amount": amount,
            "timestamp": timestamp
        }

        self.purchases[card_id].append(new_purchase)
        self.accounts[card_id]["total_purchases"] = len(self.purchases[card_id])

        return True


    def get_card_balance(self, card_id: str) -> dict | None:
        if card_id not in self.accounts:
            return None

        return {
            "credit_limit": self.accounts[card_id]["limit"],
            "amount_used": self.accounts[card_id]["amount_used"],
            "available_balance": self.accounts[card_id]["limit"] - self.accounts[card_id]["amount_used"],
            "total_purchases": len(self.purchases[card_id])
        }


c = CreditCard()

print(c.create_card("tst", 0, 2000))
print(c.get_available_balance("tst"))
print(c.make_purchase("tst", 15, 950, "ses"))
print(c.get_card_balance("tst"))
print(c.make_purchase("tst", 20, 120, "sos"))
print(c.get_card_balance("tst"))
