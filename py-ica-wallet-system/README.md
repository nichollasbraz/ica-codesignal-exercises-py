<h1>
  Wallet System
  <img src="https://i.imgur.com/Y2zRS3u.png" width="35" align="right">
</h1>

You have been hired to build the backend for a simple digital wallet. The system will evolve in four stages.


## Level 1 — Basic Operations

Implement a `Wallet` class with the following methods:

- `create_account(account_id: str, timestamp: int) -> bool`
  Creates a new account with a zero balance. Returns `True` if successfully created, `False` if the account already exists.

- `deposit(account_id: str, timestamp: int, amount: int) -> int | None`
  Deposits an amount into the account. Returns the **new balance**. If the account does not exist, returns `None`.

- `withdraw(account_id: str, timestamp: int, amount: int) -> int | None`
  Withdraws an amount from the account. Returns the **new balance**. If the account does not exist OR does not have enough balance, returns `None` (and the balance does not change).

## Level 2 — Data Processing

Add to your `Wallet`:

- `transfer(from_id: str, to_id: str, timestamp: int, amount: int) -> bool`
  Transfers money between accounts. Returns `True` if the transfer was successful. It must fail (`False`) if either account does not exist or if the balance is insufficient.

- `top_spenders(timestamp: int, n: int) -> list[str]`
  Returns the **N** account IDs that have **spent the most** (sum of withdrawals + amounts sent through transfers), ordered from highest spending to lowest spending. In case of a tie, sort by `account_id` in ascending alphabetical order.

## Level 3 — Business Rules

Add:

- `pay_with_cashback(account_id: str, timestamp: int, amount: int, cashback_percentage: float) -> str`
  Makes a payment with cashback. The cashback is **credited 24 hours later** (consider that timestamps are in minutes, so 24 hours = 1440 minutes). Returns a `payment_id` in the format `"payment{sequential_number}"` (e.g., `"payment1"`, `"payment2"`...).

- `get_payment_status(account_id: str, timestamp: int, payment_id: str) -> str | None`
  Returns the payment status: `"IN_PROGRESS"` if the cashback has not been credited yet, or `"CASHBACK_RECEIVED"` if the required time has passed. Returns `None` if the payment does not exist.


## Level 4 — Full Complexity

Add:

- `merge_accounts(account_id_1: str, account_id_2: str, timestamp: int) -> bool`
  Merges two accounts: the balance and history of `account_id_2` are transferred to `account_id_1`, and `account_id_2` is removed. Fails if either account does not exist, or if `account_id_1 == account_id_2`.

- `get_balance_timeline(account_id: str) -> list[tuple[int, int]]`
  Returns a list of tuples `(timestamp, balance)` showing how the account balance changed over time (ordered by timestamp).
