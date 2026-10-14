"""
Module 1 - Python Basics: strings, numbers, conditions, loops.
Replace each `raise NotImplementedError` with your solution.
Run `python check_progress.py` from the project folder to check your work.
"""


def reverse_words(sentence: str) -> str:
    """Reverse the ORDER of words.  "I love Python" -> "Python love I"
    Hint: str.split() and str.join()."""
    words = sentence.split()      
    words = words[::-1]           
    return " ".join(words)        


def is_palindrome(text: str) -> bool:
    """True if text reads the same backwards, ignoring case, spaces and punctuation.
    "A man, a plan, a canal: Panama" -> True
    Hint: keep only characters where ch.isalnum()."""
    
    raise NotImplementedError


def fizzbuzz(n: int) -> list:
    """Return a list of strings for 1..n: "Fizz" for multiples of 3,
    "Buzz" for multiples of 5, "FizzBuzz" for both, else the number as a string."""
    raise NotImplementedError


def count_vowels(text: str) -> int:
    """Count vowels (a, e, i, o, u), case-insensitive.  "Hello World" -> 3"""
    raise NotImplementedError


def grade(score: int) -> str:
    """90-100 -> "A", 80-89 -> "B", 70-79 -> "C", 60-69 -> "D", below 60 -> "F".
    Raise ValueError if score is outside 0..100."""
    raise NotImplementedError
