class Wallet():
    def __init__(self):
        self.accounts = {}
        self.total_spent = {}
        self.payments = {}
        self.timeline = {}
        self.payment_counter = 0


    def create_account(self, account_id: str, timestamp: int) -> bool:
        if account_id in self.accounts:
            return False
        else:
            self.accounts[account_id] = 0
            self.total_spent[account_id] = 0
            self.timeline[account_id] = [(timestamp, 0)]
            return True
            

    def deposit(self, account_id: str, timestamp: int, amount: int) -> int | None:
        if account_id in self.accounts:
            self.accounts[account_id] += amount
            self.timeline[account_id].append((timestamp, self.accounts[account_id]))
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
        self.timeline[account_id].append((timestamp, self.accounts[account_id]))
        return self.accounts[account_id]


    def transfer(self, from_id: str, to_id: str, timestamp: int, amount: int) -> bool:
        if from_id in self.accounts and to_id in self.accounts:
            if self.accounts[from_id] < amount:
                return False
            else:
                self.accounts[from_id] -= amount
                self.accounts[to_id] += amount
                self.total_spent[from_id] += amount
                self.timeline[from_id].append((timestamp, self.accounts[from_id]))
                self.timeline[to_id].append((timestamp, self.accounts[to_id]))
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

        cashback_value = round(amount * cashback_percentage / 100)

        self.payment_counter += 1
        payment_id = f"payment{self.payment_counter}"
        
        self.payments[payment_id] = {
        "account_id": account_id,
        "cashback_value": cashback_value,
        "cashback_timestamp": timestamp + 1440,
        "cashback_status": False
        }
        self.timeline[account_id].append((timestamp, self.accounts[account_id]))
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

            self.timeline[payment["account_id"]].append((timestamp, self.accounts[payment["account_id"]]))

        return "CASHBACK_RECEIVED" if payment["cashback_status"] else "IN_PROGRESS"
        

    def merge_accounts(self, account_id_1: str, account_id_2: str, timestamp: int) -> bool:
        if account_id_1 not in self.accounts or account_id_2 not in self.accounts:
            return False
        if account_id_1 == account_id_2:
            return False    

        self.accounts[account_id_1] += self.accounts[account_id_2]
        self.total_spent[account_id_1] += self.total_spent[account_id_2]

        timeline_1 = self.timeline[account_id_1]
        timeline_2 = self.timeline[account_id_2]
        timelines_combined = timeline_1  + timeline_2
        timelines_combined.sort()

        self.timeline[account_id_1] = timelines_combined

        self.timeline[account_id_1].append((timestamp, self.accounts[account_id_1]))

        for payment in self.payments.values():
            if payment["account_id"] == account_id_2:
                payment["account_id"] = account_id_1
        
        del self.accounts[account_id_2]
        del self.total_spent[account_id_2]
        
        return True


    def get_balance_timeline(self, account_id: str) -> list[tuple[int, int]]:
        return sorted(self.timeline[account_id])

    