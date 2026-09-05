class CheckingAccount():
    def __init__(self):
        self.accounts = {}
        self.withdrawals = {}
        self.total_deposits = 0
        self.total_withdrawals = 0
        self.transaction_counter = 0

    def create_account(self, account_id: str, timestamp: int, initial_balance: int) -> bool:
        if account_id not in self.accounts:
            self.accounts[account_id] = initial_balance
            self.withdrawals[account_id] = []
            
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
            self.accounts[account_id] += amount
            self.total_deposits += amount
            

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
        
        self.accounts[account_id] -= amount
        self.total_withdrawals += amount

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

c = CheckingAccount()
print(c.create_account("malagoli", 0, 2000))
print(c.get_balance("malagoli"))
print(c.deposit("malagoli", 0, 500))
print(c.get_account_info("malagoli"))
print(c.withdraw("malagoli", 10, 200))
print(c.get_account_info("malagoli"))
print(c.withdraw("malagoli", 11, 200))
print(c.get_account_info("malagoli"))
print(c.withdraw("malagoli", 12, 20000))
print(c.get_account_info("malagoli"))
