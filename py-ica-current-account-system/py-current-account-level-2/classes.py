class CheckingAccount():
    def __init__(self):
        self.accounts = {}
        self.withdrawals = {}
        self.transactions = {}
        self.total_deposits = 0
        self.total_withdrawals = 0
        self.transaction_counter = len(self.transactions)

    def create_account(self, account_id: str, timestamp: int, initial_balance: int) -> bool:
        if account_id not in self.accounts:
            self.accounts[account_id] = initial_balance
            self.withdrawals[account_id] = []
            self.transactions[account_id] = []
            
            return True
        else:
            return False

    def get_balance(self, account_id: str) -> int | None:
        if account_id not in self.accounts:
            return None
        else:
            return self.accounts[account_id]

    def deposit(self, account_id: str, timestamp: int, amount: int) -> int | None:
        if account_id not in self.accounts:
            return None
        else:
            new_transaction = {
                "type":"deposit",
                "amount": amount,
                "timestamp": timestamp,
                "balance_after": self.accounts[account_id]
            }

            self.transactions[account_id].append(new_transaction)

            self.accounts[account_id] += amount
            self.total_deposits += amount
            self.transaction_counter += 1
            
            return self.accounts[account_id]

    def withdraw(self, account_id: str, timestamp: int, amount: int) -> int | None:
        if account_id not in self.accounts:
            return None
        if amount > self.accounts[account_id]:
            new_withdrawal_none = {
                        "amount":amount,
                        "timestamp":timestamp,
                        "status":"BLOCKED"
                    }
            self.withdrawals[account_id].append(new_withdrawal_none)

            return None

        new_transaction = {
            "type":"withdraw",
            "amount": amount,
            "timestamp": timestamp,
            "balance_after": self.accounts[account_id]
            }
                
        self.transactions[account_id].append(new_transaction)
        
        self.accounts[account_id] -= amount
        self.total_withdrawals += amount
        self.transaction_counter += 1

        new_withdrawal = {
            "amount":amount,
            "timestamp":timestamp,
            "status":"SUCCESS"
        }

        self.withdrawals[account_id].append(new_withdrawal)

        return self.accounts[account_id]

    def get_account_info(self, account_id: str) -> dict | None:
        if account_id not in self.accounts:
            return None
        else:
            return {
                "account_id": account_id,
                "balance": self.accounts[account_id],
                "total_deposits": self.total_deposits,
                "total_withdrawals": self.total_withdrawals,
                "total_transactions": self.transaction_counter 
            }

    def get_transaction_history(self, account_id: str, limit: int) -> list[dict]:
        if account_id not in self.accounts:
            return None
        if len(self.transactions[account_id]) == 0:
            return None
        else:
            srtHistory = sorted(self.transactions[account_id], key=lambda item: -item["timestamp"])

            return srtHistory[:limit]


    def daily_withdrawal_total(self, account_id: str, timestamp: int) -> int:
        if account_id not in self.accounts:
            return None
        else:
            total = 0

            for transaction in self.transactions[account_id]:
                if transaction["type"] == "withdraw" and transaction["timestamp"] == timestamp:
                    total += transaction["amount"]

            return total
                

    def largest_transaction(self, account_id: str) -> dict | None:
        if account_id not in self.accounts:
            return None
        if len(self.transactions[account_id]) == 0:
            return None
        else:
            biggestAmount = 0
            biggestType = ""
            biggestTimestamp = 0

            for transaction in self.transactions[account_id]:   
                if transaction["amount"] > biggestAmount:
                    biggestAmount = transaction["amount"]
                    biggestType = transaction["type"]
                    biggestTimestamp = transaction["timestamp"]

            return {
                "type": biggestType,
                "amount": biggestAmount,
                "timestamp": biggestTimestamp
            }
        

c = CheckingAccount()
print(c.create_account("malagoli", 0, 2000))
print(c.get_balance("malagoli"))
print(c.deposit("malagoli", 30, 200))
print(c.get_account_info("malagoli"))
print(c.withdraw("malagoli", 22, 400))
print(c.get_account_info("malagoli"))
print(c.withdraw("malagoli", 22, 200))
print(c.get_account_info("malagoli"))
print(c.withdraw("malagoli", 12, 20000))
print(c.get_account_info("malagoli"))
print(c.get_transaction_history("malagoli", 22))
print(c.daily_withdrawal_total("malagoli", 22))
print(c.largest_transaction("malagoli"))
