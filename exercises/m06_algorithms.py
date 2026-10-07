"""
Module 6 - Problem Solving: classic algorithms that come up in code reviews
and interviews. Think about efficiency, not just correctness.
"""


def two_sum(nums: list, target: int) -> tuple:
    """Return indices (i, j), i < j, where nums[i] + nums[j] == target.
    Return None if no pair exists. Aim for O(n) using a dict."""
    raise NotImplementedError


def binary_search(sorted_nums: list, target: int) -> int:
    """Return the index of target in a sorted list, or -1. Don't use .index()."""
    raise NotImplementedError


def is_balanced(brackets: str) -> bool:
    """True if all (), [], {} are correctly matched and nested.
    "{[()]}" -> True, "([)]" -> False. Hint: use a list as a stack."""
    raise NotImplementedError


def fibonacci(n: int) -> int:
    """Return the n-th Fibonacci number (fib(0)=0, fib(1)=1).
    Must be fast for n=200 (no naive recursion)."""
    raise NotImplementedError


def most_frequent(items: list):
    """Return the most common item. On a tie, return the one that appears FIRST."""
    raise NotImplementedError


def chunk(items: list, size: int) -> list:
    """Split into chunks.  chunk([1,2,3,4,5], 2) -> [[1,2],[3,4],[5]]
    Raise ValueError if size < 1."""
    raise NotImplementedError
