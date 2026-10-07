"""
Module 4 - Object-Oriented Programming: classes, properties, inheritance,
dunder methods.
"""


class InsufficientFundsError(Exception):
    """Raised when a withdrawal is larger than the balance. (Already done for you.)"""


class BankAccount:
    """
    - BankAccount(owner, balance=0)
    - .owner, .balance attributes
    - deposit(amount): amount must be > 0 else raise ValueError
    - withdraw(amount): amount must be > 0 else ValueError;
      if amount > balance raise InsufficientFundsError
    - .history: list of tuples like ("deposit", 100) / ("withdraw", 40)
    - str(account) -> "Asha: 60.00"  (2 decimal places)
    """

    def __init__(self, owner, balance=0):
        raise NotImplementedError


class SavingsAccount(BankAccount):
    """
    Inherits from BankAccount.
    - SavingsAccount(owner, balance=0, rate=0.05)
    - add_interest(): deposits balance * rate (and records it in history as a deposit)
    """

    def __init__(self, owner, balance=0, rate=0.05):
        raise NotImplementedError


class Rectangle:
    """
    - Rectangle(width, height); both must be > 0 else ValueError
    - .area property and .perimeter property (not methods!)
    - Two rectangles are equal (==) if width and height match
    - Rectangles can be sorted by area (implement __lt__)
    """

    def __init__(self, width, height):
        raise NotImplementedError
