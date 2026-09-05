class CreditCard():
    def __init__(self):
        self.accounts = {}
        self.purchases = {}
        self.invoices = {}
        self.invoice_counter = 0


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


    def top_spending_categories(self, card_id: str, n: int) -> list[tuple[str, int]]:
        if card_id not in self.accounts:
            return None

        categories = {}

        for purchase in self.purchases[card_id]:
            category = purchase["category"]
            amount = purchase["amount"]

            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount

        doubles = categories.items()
        srtDoubles = sorted(doubles, key=lambda item : (-item[1], item[0]))
        result = srtDoubles[:n]

        return result


    def get_purchase_history(self, card_id: str) -> list[dict]:
        if card_id not in self.accounts:
            return None

        srtHistory = sorted(self.purchases[card_id], key=lambda item: -item["timestamp"])

        return srtHistory  


    def create_invoice(self, card_id: str, timestamp: int, invoice_timestamp: int) -> str | None:
        if card_id not in self.accounts:
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
        "purchases": old_purchases,     
        "total_amount": total_amount,    
        "paid_amount": 0,
        "remaining_amount": total_amount,
        "status": "OPEN",
        "due_timestamp": invoice_timestamp + 2880
        }

        return invoice_id


    def pay_invoice(self, card_id: str, timestamp: int, invoice_id: str, amount: int) -> bool:
        if card_id not in self.accounts:
            return False

        if invoice_id not in self.invoices:
            return False

        if amount <= 0 or amount > self.invoices[invoice_id]["remaining_amount"]:
            return False

        self.invoices[invoice_id]["remaining_amount"] -= amount
        self.invoices[invoice_id]["paid_amount"] += amount

        if self.invoices[invoice_id]["remaining_amount"] == 0:
            self.invoices[invoice_id]["status"] = "PAID"
        else:
            self.invoices[invoice_id]["status"] = "PARTIALLY_PAID"

        return True


    def get_invoice_status(self, card_id: str, invoice_id: str) -> dict | None:
        if card_id not in self.accounts:
            return None

        if invoice_id not in self.invoices:
            return None

        invoice = self.invoices[invoice_id]

        return { 
            "invoice_id": invoice_id,
            "total_amount": invoice["total_amount"],
            "paid_amount": invoice["paid_amount"],
            "remaining_amount": invoice["remaining_amount"],
            "status": invoice["status"],
            "due_timestamp": invoice["due_timestamp"]
        }    

    