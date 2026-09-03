class Wallet():
    def __init__(self):
        self.accounts = {}
        self.total_spent = {}


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

        