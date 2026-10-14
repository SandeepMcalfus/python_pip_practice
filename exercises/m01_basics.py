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
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def fizzbuzz(n: int) -> list:
    """Return a list of strings for 1..n: "Fizz" for multiples of 3,
    "Buzz" for multiples of 5, "FizzBuzz" for both, else the number as a string."""
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


def count_vowels(text: str) -> int:
    """Count vowels (a, e, i, o, u), case-insensitive.  "Hello World" -> 3"""
    return sum(1 for ch in text.lower() if ch in "aeiou")


def grade(score: int) -> str:
    """90-100 -> "A", 80-89 -> "B", 70-79 -> "C", 60-69 -> "D", below 60 -> "F".
    Raise ValueError if score is outside 0..100."""
    if score < 0 or score > 100:
        raise ValueError(f"score must be between 0 and 100, got {score}")
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


# ---------------------------------------------------------------------------
# Numbers & arithmetic  (+ - * / // % **, round, f-string formatting)
# ---------------------------------------------------------------------------

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit:  F = C * 9/5 + 32.   100 -> 212.0"""
    return celsius * 9 / 5 + 32


def is_even(n: int) -> bool:
    """True if n is even.  4 -> True, 7 -> False.   Hint: the % operator."""
    return n % 2 == 0


def split_minutes(total_minutes: int) -> tuple:
    """Turn a number of minutes into (hours, minutes).  135 -> (2, 15)
    Hint: // and %, or the built-in divmod()."""
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return (hours, minutes)


def sum_of_digits(n: int) -> int:
    """Add up the digits of n (ignore the sign).  1234 -> 10,  -56 -> 11"""
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def format_price(amount: float) -> str:
    """Format as dollars with 2 decimals and thousands separators.
    3.5 -> "$3.50",  1234.5 -> "$1,234.50"
    Hint: f"{amount:,.2f}" """
    return f"${amount:,.2f}"


# ---------------------------------------------------------------------------
# Types & conversion  (int(), float(), str(), isinstance)
# ---------------------------------------------------------------------------

def to_number(text: str):
    """Convert text to an int if it's a whole number, otherwise a float.
    Surrounding spaces are ignored.  "42" -> 42,  "3.5" -> 3.5,  " 7 " -> 7"""
    text = text.strip()
    if "." in text:
        return float(text)
    return int(text)


# ---------------------------------------------------------------------------
# Strings  (methods, slicing, indexing, ord/chr, building strings in a loop)
# ---------------------------------------------------------------------------

def capitalize_words(sentence: str) -> str:
    """Capitalize the first letter of every word, lowercase the rest.
    "hello wORLD" -> "Hello World"   Hint: str.capitalize()."""
    words = sentence.split()
    return " ".join(word.capitalize() for word in words)


def initials(full_name: str) -> str:
    """Uppercase initials, each followed by a dot.
    "Ada Lovelace" -> "A.L.",  "guido van rossum" -> "G.V.R." """
    result = ""
    for word in full_name.split():
        result += word[0].upper() + "."
    return result


def normalize_spaces(text: str) -> str:
    """Remove leading/trailing spaces and collapse repeated spaces into one.
    "  hello    world  " -> "hello world" """
    return " ".join(text.split())


def mask_card(card_number: str) -> str:
    """Replace every character except the last 4 with "*".
    "1234567812345678" -> "************5678".  4 or fewer chars -> unchanged.
    Hint: slicing and "*" * count."""
    if len(card_number) <= 4:
        return card_number
    hidden = len(card_number) - 4
    return "*" * hidden + card_number[-4:]


def is_anagram(a: str, b: str) -> bool:
    """True if a and b use exactly the same letters, ignoring case and spaces.
    "Listen", "Silent" -> True,   "Dormitory", "dirty room" -> True
    Hint: sorted()."""
    a = a.replace(" ", "").lower()
    b = b.replace(" ", "").lower()
    return sorted(a) == sorted(b)


def longest_word(sentence: str) -> str:
    """Return the longest word. On a tie, return the first one. "" -> ""
    "I love programming in Python" -> "programming" """
    longest = ""
    for word in sentence.split():
        if len(word) > len(longest):
            longest = word
    return longest


def compress(text: str) -> str:
    """Run-length encode: each character followed by how many times it repeats in a row.
    "aaabbc" -> "a3b2c1",  "abc" -> "a1b1c1",  "" -> "" """
    if not text:
        return ""
    result = ""
    current = text[0]
    count = 0
    for ch in text:
        if ch == current:
            count += 1
        else:
            result += current + str(count)
            current = ch
            count = 1
    result += current + str(count)
    return result


def caesar_cipher(text: str, shift: int) -> str:
    """Shift every letter by `shift` places in the alphabet, wrapping around.
    Keep upper/lower case; leave non-letters unchanged. shift can be negative.
    "abc", 1 -> "bcd",   "xyz", 3 -> "abc",   "Hello, World!", 3 -> "Khoor, Zruog!"
    Hint: ord(), chr() and % 26."""
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            position = (ord(ch) - base + shift) % 26
            result += chr(base + position)
        else:
            result += ch
    return result


# ---------------------------------------------------------------------------
# Conditions  (if / elif / else, and / or / not, comparison chaining)
# ---------------------------------------------------------------------------

def is_leap_year(year: int) -> bool:
    """Leap year: divisible by 4, except centuries, unless divisible by 400.
    2024 -> True, 2023 -> False, 1900 -> False, 2000 -> True"""
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


def max_of_three(a: int, b: int, c: int) -> int:
    """Return the largest of three numbers WITHOUT using max() or sorted()."""
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest


def triangle_type(a: float, b: float, c: float) -> str:
    """Return "equilateral" (3 equal sides), "isosceles" (exactly 2 equal) or "scalene".
    Return "invalid" if any side is <= 0 or two sides don't add up to MORE than the third.
    (3, 4, 5) -> "scalene",   (1, 2, 3) -> "invalid" """
    if a <= 0 or b <= 0 or c <= 0:
        return "invalid"
    if a + b <= c or a + c <= b or b + c <= a:
        return "invalid"
    if a == b == c:
        return "equilateral"
    if a == b or b == c or a == c:
        return "isosceles"
    return "scalene"


def bmi_category(weight_kg: float, height_m: float) -> str:
    """BMI = weight / height squared.
    below 18.5 -> "Underweight", below 25 -> "Normal", below 30 -> "Overweight", else "Obese"."""
    bmi = weight_kg / height_m ** 2
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Normal"
    if bmi < 30:
        return "Overweight"
    return "Obese"


# ---------------------------------------------------------------------------
# Loops  (for, while, range, break/continue, nested loops, accumulators)
# ---------------------------------------------------------------------------

def factorial(n: int) -> int:
    """n! using a loop (not math.factorial).  0 -> 1,  5 -> 120.
    Raise ValueError if n is negative."""
    if n < 0:
        raise ValueError(f"factorial is not defined for negative numbers, got {n}")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(n: int) -> bool:
    """True if n is a prime number.  2 -> True, 15 -> False, 1 -> False.
    Hint: you only need to check divisors up to the square root of n."""
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def fibonacci(n: int) -> list:
    """Return the first n Fibonacci numbers.  7 -> [0, 1, 1, 2, 3, 5, 8],  0 -> []"""
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


def multiplication_table(n: int) -> list:
    """Return 10 strings for n x 1 up to n x 10.
    3 -> ["3 x 1 = 3", "3 x 2 = 6", ..., "3 x 10 = 30"]"""
    return [f"{n} x {i} = {n * i}" for i in range(1, 11)]


def reverse_number(n: int) -> int:
    """Reverse the digits of a non-negative int using math, not strings.
    1234 -> 4321,  1200 -> 21.   Hint: a while loop with % 10 and // 10."""
    reversed_n = 0
    while n > 0:
        reversed_n = reversed_n * 10 + n % 10
        n //= 10
    return reversed_n


def collatz_steps(n: int) -> int:
    """Count steps to reach 1: if n is even, n = n // 2, otherwise n = 3 * n + 1.
    1 -> 0,  6 -> 8  (6, 3, 10, 5, 16, 8, 4, 2, 1)"""
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps


def gcd(a: int, b: int) -> int:
    """Greatest common divisor using Euclid's algorithm (not math.gcd):
    while b is not 0:  a, b = b, a % b.     12, 18 -> 6"""
    while b != 0:
        a, b = b, a % b
    return a


def right_triangle(n: int) -> str:
    """Build a triangle of stars with n rows, joined by newlines.
    3 -> "*\\n**\\n***",   0 -> "" """
    rows = []
    for i in range(1, n + 1):
        rows.append("*" * i)
    return "\n".join(rows)
