class Wallet():
    def __init__(self):
        self.accounts = {}
        self.total_spent = {}
        self.payments = {}
        self.payment_counter = 0

    def create_account(self, account_id: str, timestamp: int) -> bool:
        if account_id in self.accounts:
            return False
        else:
            self.accounts[account_id] = 0
            self.total_spent[account_id] = 0
            return True
            

    def deposit(self, account_id: str, timestamp: int, amount: int) -> int | None:
        if account_id in self.accounts:
            self.accounts[account_id] += amount
            return self.accounts[account_id]
        else:
            return None
            
        
    def withdraw(self, account_id: str, timestamp: int, amount: int) -> int | None:
        if account_id not in self.accounts:
            return None
        if self.accounts[account_id] < amount:
            return None
        self.accounts[account_id] -= amount
        self.total_spent[account_id] += amount
        return self.accounts[account_id]


    def transfer(self, from_id: str, to_id: str, timestamp: int, amount: int) -> bool:
        if from_id in self.accounts and to_id in self.accounts:
            if self.accounts[from_id] < amount:
                return False
            else:
                self.accounts[from_id] -= amount
                self.accounts[to_id] += amount
                self.total_spent[from_id] += amount
                return True
        else:
            return False


    def top_spenders(self, timestamp: int, n: int) -> list[str]:
        doubles = self.total_spent.items()
        orderedDoubles = sorted(doubles, key=lambda item: (-item[1], item[0]))
        result = [account_id for account_id, amount in orderedDoubles [:n]]
        return result


    def pay_with_cashback(self, account_id: str, timestamp: int, amount: int, cashback_percentage: float) -> str:
        if account_id not in self.accounts:
            return None
        if self.accounts[account_id] < amount:
            return None
        self.accounts[account_id] -= amount
        self.total_spent[account_id] += amount

        self.cashback_value = round(amount * cashback_percentage / 100)

        self.payment_counter += 1
        payment_id = f"payment{self.payment_counter}"
        
        self.payments[payment_id] = {
        "account_id": account_id,
        "cashback_value": self.cashback_value,
        "cashback_timestamp": timestamp + 1440,
        "cashback_status": False
        }
        return payment_id

    def get_payment_status(self, account_id: str, timestamp: int, payment_id: str) -> str | None:
        if account_id not in self.accounts:
            return None
        if payment_id not in self.payments:
            return None

        payment = self.payments[payment_id]
        if payment["account_id"] != account_id:
            return None

        if timestamp >= payment["cashback_timestamp"] and not payment["cashback_status"]:
            self.accounts[payment["account_id"]] += payment["cashback_value"]
            payment["cashback_status"] = True

        return "CASHBACK_RECEIVED" if payment["cashback_status"] else "IN_PROGRESS"
        
    