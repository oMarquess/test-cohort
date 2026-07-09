class BankAccount:
    """A simple class representing a bank account to learn Object-Oriented Programming (OOP)."""
    
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> float:
        """Deposits money into the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        """Withdraws money from the account if funds are sufficient."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance

    def __str__(self) -> str:
        return f"Account owner: {self.owner}, Balance: ${self.balance:.2f}"


if __name__ == "__main__":
    # Create an account
    account = BankAccount("Alice", 100.0)
    print(account)

    # Deposit money
    account.deposit(50.0)
    print(f"After deposit: {account}")

    # Withdraw money
    account.withdraw(30.0)
    print(f"After withdrawal: {account}")
