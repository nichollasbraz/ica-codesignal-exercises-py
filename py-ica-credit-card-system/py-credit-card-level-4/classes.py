class CreditCard():

    def __init__(self):
        self.cards = {}
        self.purchases = {}
        self.invoices = {}
        self.invoice_counter = 0


    def create_card(self, card_id: str, timestamp: int, credit_limit: int) -> bool:
        if card_id not in self.cards:
            self.cards[card_id] = {
                "credit_limit": credit_limit,
                "amount_used": 0,
                "total_purchases": len(self.purchases)
            }
            self.purchases[card_id] = []

            return True
        else:
            return False

    def get_available_balance(self, card_id: str) -> int | None:
        if card_id not in self.cards:
            return None
        else:
            available = self.cards[card_id]["credit_limit"] - self.cards[card_id]["amount_used"]
            return available

    def make_purchase(self, card_id: str, timestamp: int, amount: int, category: str) -> bool:
        if card_id not in self.cards:
            return False

        available = self.cards[card_id]["credit_limit"] - self.cards[card_id]["amount_used"]
        if amount > available:
            return False

        self.cards[card_id]["amount_used"] += amount

        new_purchase = {
            "category": category,
            "timestamp": timestamp,
            "amount": amount,                
        }

        self.purchases[card_id].append(new_purchase)
        self.cards[card_id]["total_purchases"] = len(self.purchases[card_id])

        return True

    def get_card_balance(self, card_id: str) -> dict | None:
        if card_id not in self.cards:
            return None

        return {
            "credit_limit": self.cards[card_id]["credit_limit"],
            "amount_used": self.cards[card_id]["amount_used"],
            "available_balance": self.cards[card_id]["credit_limit"] - self.cards[card_id]["amount_used"],
            "total_purchases": self.cards[card_id]["total_purchases"]
        }

    def top_spending_categories(self, card_id: str, n: int) -> list[tuple[str, int]]:
        if card_id not in self.cards:
            return None

        categories = {}

        for purchase in self.purchases[card_id]:
            category = purchase["category"]
            amount = purchase["amount"]

            if category not in categories:
                categories[category] = amount
            else:
                categories[category] += amount

        doubles = categories.items()
        srtDoubles = sorted(doubles, key=lambda item : (-item[1], item[0]))
        result = srtDoubles[:n]

        return result

    def spending_by_period(self, card_id: str, start_timestamp: int, end_timestamp: int) -> int:
        if card_id not in self.cards:
            return None

        total = 0

        for purchase in self.purchases[card_id]:
            if purchase["timestamp"] >= start_timestamp and purchase["timestamp"] <= end_timestamp:
                total += purchase["amount"]

        return total

    def get_purchase_history(self, card_id: str) -> list[dict]:
        if card_id not in self.cards:
            return False

        srtResult = sorted(self.purchases[card_id], key=lambda item: -item["timestamp"])
        return srtResult

    def create_invoice(self, card_id: str, timestamp: int, invoice_timestamp: int) -> str | None:
        if card_id not in self.cards:
            return None 

        old_purchases = []

        for purchase in self.purchases[card_id]:
            if purchase["timestamp"] < invoice_timestamp:
                old_purchases.append(purchase)

        if len(old_purchases) == 0:
            return None

        total_amount = sum(p["amount"] for p in old_purchases)

        self.invoice_counter += 1

        invoice_id = f"invoice{self.invoice_counter}"

        self.invoices[invoice_id] = {
            "card_id": card_id,
            "total_amount": total_amount,
            "paid_amount": 0,
            "remaining_amount": total_amount,
            "invoice_timestamp": invoice_timestamp + 2880,
            "invoice_status": "OPEN"
        }

        return invoice_id


    def pay_invoice(self, card_id: str, timestamp: int, invoice_id: str, amount: int) -> bool:
        if card_id not in self.cards:
            return False

        if invoice_id not in self.invoices:
            return False

        if self.invoices[invoice_id]["remaining_amount"] < amount or amount <= 0:
            return False

        self.invoices[invoice_id]["paid_amount"] += amount
        self.invoices[invoice_id]["remaining_amount"] -= amount

        if self.invoices[invoice_id]["remaining_amount"] == 0:
            self.invoices[invoice_id]["invoice_status"] = "PAID"
            return True
        else:
            self.invoices[invoice_id]["invoice_status"] = "PARTIALLY_PAID"
            return True

    def get_invoice_status(self, card_id: str, invoice_id: str) -> dict | None:
        if card_id not in self.cards: 
            return None         

        if invoice_id not in self.invoices:
            return None

        return {
            "invoice_id": invoice_id,
            "total_amount": self.invoices[invoice_id]["total_amount"],
            "paid_amount": self.invoices[invoice_id]["paid_amount"],
            "remaining_amount": self.invoices[invoice_id]["remaining_amount"],
            "invoice_timestamp": self.invoices[invoice_id]["invoice_timestamp"],
            "invoice_status": self.invoices[invoice_id]["invoice_status"]
        }

c = CreditCard()

print(c.create_card("Malagoli", 0, 2000))
print(c.__dict__)
print(c.get_available_balance("Malagoli"))
print(c.make_purchase("Malagoli", 0, 1200, "uber"))
print(c.get_card_balance("Malagoli"))
print(c.top_spending_categories("Malagoli", 2))
print(c.spending_by_period("Malagoli", 0, 0))
print(c.get_purchase_history("Malagoli"))
print(c.create_invoice("Malagoli", 0, 40))
print(c.pay_invoice("Malagoli", 0, "invoice1", 300))
print(c.get_invoice_status("Malagoli", "invoice1"))
print(c.pay_invoice("Malagoli", 0, "invoice1", 900))
print(c.get_invoice_status("Malagoli", "invoice1"))
