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
