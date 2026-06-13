"""Simple bank account MCP server built with FastMCP."""

import logging

from fastmcp import FastMCP

logging.getLogger("fastmcp").setLevel(logging.WARNING)

mcp = FastMCP(name="Bank Account Server")


class BankAccount:
    """In-memory bank account with deposit, withdraw, and balance."""

    def __init__(self, initial_balance: float = 0.0) -> None:
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self._balance = initial_balance

    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        return self._balance

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        return self._balance

    @property
    def balance(self) -> float:
        return self._balance


_account = BankAccount()


@mcp.tool
def deposit(amount: float) -> dict[str, float]:
    """Deposit money into the bank account."""
    new_balance = _account.deposit(amount)
    return {"deposited": amount, "balance": new_balance}


@mcp.tool
def withdraw(amount: float) -> dict[str, float]:
    """Withdraw money from the bank account."""
    new_balance = _account.withdraw(amount)
    return {"withdrawn": amount, "balance": new_balance}


@mcp.tool
def get_balance() -> dict[str, float]:
    """Return the current account balance."""
    return {"balance": _account.balance}


if __name__ == "__main__":
    mcp.run(show_banner=False)
