import unittest
from exercises import m01_basics as m


class TestBasics(unittest.TestCase):
    def test_reverse_words(self):
        self.assertEqual(m.reverse_words("I love Python"), "Python love I")
        self.assertEqual(m.reverse_words("one"), "one")

    def test_is_palindrome(self):
        self.assertTrue(m.is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(m.is_palindrome("racecar"))
        self.assertFalse(m.is_palindrome("python"))

    def test_fizzbuzz(self):
        self.assertEqual(m.fizzbuzz(5), ["1", "2", "Fizz", "4", "Buzz"])
        self.assertEqual(m.fizzbuzz(15)[-1], "FizzBuzz")

    def test_count_vowels(self):
        self.assertEqual(m.count_vowels("Hello World"), 3)
        self.assertEqual(m.count_vowels("AEIOU xyz"), 5)
        self.assertEqual(m.count_vowels(""), 0)

    def test_grade(self):
        self.assertEqual(m.grade(95), "A")
        self.assertEqual(m.grade(80), "B")
        self.assertEqual(m.grade(79), "C")
        self.assertEqual(m.grade(60), "D")
        self.assertEqual(m.grade(0), "F")
        with self.assertRaises(ValueError):
            m.grade(101)
        with self.assertRaises(ValueError):
            m.grade(-1)

    # --- Numbers & arithmetic -------------------------------------------

    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(m.celsius_to_fahrenheit(0), 32)
        self.assertAlmostEqual(m.celsius_to_fahrenheit(100), 212)
        self.assertAlmostEqual(m.celsius_to_fahrenheit(-40), -40)
        self.assertAlmostEqual(m.celsius_to_fahrenheit(37), 98.6)

    def test_is_even(self):
        self.assertTrue(m.is_even(4))
        self.assertFalse(m.is_even(7))
        self.assertTrue(m.is_even(0))
        self.assertTrue(m.is_even(-2))

    def test_split_minutes(self):
        self.assertEqual(m.split_minutes(135), (2, 15))
        self.assertEqual(m.split_minutes(59), (0, 59))
        self.assertEqual(m.split_minutes(120), (2, 0))

    def test_sum_of_digits(self):
        self.assertEqual(m.sum_of_digits(1234), 10)
        self.assertEqual(m.sum_of_digits(0), 0)
        self.assertEqual(m.sum_of_digits(-56), 11)

    def test_format_price(self):
        self.assertEqual(m.format_price(3.5), "$3.50")
        self.assertEqual(m.format_price(1234.5), "$1,234.50")
        self.assertEqual(m.format_price(0), "$0.00")

    # --- Types & conversion ---------------------------------------------

    def test_to_number(self):
        self.assertEqual(m.to_number("42"), 42)
        self.assertIsInstance(m.to_number("42"), int)
        self.assertEqual(m.to_number("3.5"), 3.5)
        self.assertIsInstance(m.to_number("3.5"), float)
        self.assertEqual(m.to_number(" 7 "), 7)

    # --- Strings ----------------------------------------------------------

    def test_capitalize_words(self):
        self.assertEqual(m.capitalize_words("hello wORLD"), "Hello World")
        self.assertEqual(m.capitalize_words("python"), "Python")

    def test_initials(self):
        self.assertEqual(m.initials("Ada Lovelace"), "A.L.")
        self.assertEqual(m.initials("guido van rossum"), "G.V.R.")

    def test_normalize_spaces(self):
        self.assertEqual(m.normalize_spaces("  hello    world  "), "hello world")
        self.assertEqual(m.normalize_spaces("one"), "one")
        self.assertEqual(m.normalize_spaces(""), "")

    def test_mask_card(self):
        self.assertEqual(m.mask_card("1234567812345678"), "************5678")
        self.assertEqual(m.mask_card("98765"), "*8765")
        self.assertEqual(m.mask_card("1234"), "1234")

    def test_is_anagram(self):
        self.assertTrue(m.is_anagram("Listen", "Silent"))
        self.assertTrue(m.is_anagram("Dormitory", "dirty room"))
        self.assertFalse(m.is_anagram("hello", "world"))

    def test_longest_word(self):
        self.assertEqual(m.longest_word("I love programming in Python"), "programming")
        self.assertEqual(m.longest_word("cat dog"), "cat")
        self.assertEqual(m.longest_word(""), "")

    def test_compress(self):
        self.assertEqual(m.compress("aaabbc"), "a3b2c1")
        self.assertEqual(m.compress("abc"), "a1b1c1")
        self.assertEqual(m.compress("aabaa"), "a2b1a2")
        self.assertEqual(m.compress(""), "")

    def test_caesar_cipher(self):
        self.assertEqual(m.caesar_cipher("abc", 1), "bcd")
        self.assertEqual(m.caesar_cipher("xyz", 3), "abc")
        self.assertEqual(m.caesar_cipher("Hello, World!", 3), "Khoor, Zruog!")
        self.assertEqual(m.caesar_cipher("bcd", -1), "abc")

    # --- Conditions -------------------------------------------------------

    def test_is_leap_year(self):
        self.assertTrue(m.is_leap_year(2024))
        self.assertFalse(m.is_leap_year(2023))
        self.assertFalse(m.is_leap_year(1900))
        self.assertTrue(m.is_leap_year(2000))

    def test_max_of_three(self):
        self.assertEqual(m.max_of_three(1, 5, 3), 5)
        self.assertEqual(m.max_of_three(9, 2, 4), 9)
        self.assertEqual(m.max_of_three(-1, -5, -3), -1)
        self.assertEqual(m.max_of_three(2, 2, 2), 2)

    def test_triangle_type(self):
        self.assertEqual(m.triangle_type(3, 3, 3), "equilateral")
        self.assertEqual(m.triangle_type(3, 3, 5), "isosceles")
        self.assertEqual(m.triangle_type(3, 4, 5), "scalene")
        self.assertEqual(m.triangle_type(1, 2, 3), "invalid")
        self.assertEqual(m.triangle_type(0, 1, 1), "invalid")

    def test_bmi_category(self):
        self.assertEqual(m.bmi_category(50, 1.8), "Underweight")
        self.assertEqual(m.bmi_category(70, 1.75), "Normal")
        self.assertEqual(m.bmi_category(85, 1.75), "Overweight")
        self.assertEqual(m.bmi_category(110, 1.75), "Obese")

    # --- Loops ------------------------------------------------------------

    def test_factorial(self):
        self.assertEqual(m.factorial(0), 1)
        self.assertEqual(m.factorial(5), 120)
        with self.assertRaises(ValueError):
            m.factorial(-1)

    def test_is_prime(self):
        for n in (2, 3, 17, 97):
            self.assertTrue(m.is_prime(n), n)
        for n in (0, 1, 4, 15, 49):
            self.assertFalse(m.is_prime(n), n)

    def test_fibonacci(self):
        self.assertEqual(m.fibonacci(7), [0, 1, 1, 2, 3, 5, 8])
        self.assertEqual(m.fibonacci(1), [0])
        self.assertEqual(m.fibonacci(0), [])

    def test_multiplication_table(self):
        table = m.multiplication_table(3)
        self.assertEqual(len(table), 10)
        self.assertEqual(table[0], "3 x 1 = 3")
        self.assertEqual(table[-1], "3 x 10 = 30")

    def test_reverse_number(self):
        self.assertEqual(m.reverse_number(1234), 4321)
        self.assertEqual(m.reverse_number(1200), 21)
        self.assertEqual(m.reverse_number(7), 7)

    def test_collatz_steps(self):
        self.assertEqual(m.collatz_steps(1), 0)
        self.assertEqual(m.collatz_steps(6), 8)
        self.assertEqual(m.collatz_steps(27), 111)

    def test_gcd(self):
        self.assertEqual(m.gcd(12, 18), 6)
        self.assertEqual(m.gcd(17, 5), 1)
        self.assertEqual(m.gcd(0, 9), 9)

    def test_right_triangle(self):
        self.assertEqual(m.right_triangle(3), "*\n**\n***")
        self.assertEqual(m.right_triangle(1), "*")
        self.assertEqual(m.right_triangle(0), "")
