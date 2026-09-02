class Wallet():
    def __init__(self):
        self.accounts = {}


    def create_account(self, account_id: str, timestamp: int) -> bool:
        if account_id in self.accounts:
            return False
        else:
            self.accounts[account_id] = 0
            return True
        

    def deposit(self, account_id: str, timestamp: int, amount: int) -> int | None:
        if account_id in self.accounts:
            self.accounts[account_id] += amount
            return self.accounts[account_id]
        else:
            return None
        
    
    def withdraw(self, account_id: str, timestamp: int, amount: int) -> int | None:
        if account_id in self.accounts:
            self.accounts[account_id] -= amount
            return self.accounts[account_id]
        else:
            return None

        