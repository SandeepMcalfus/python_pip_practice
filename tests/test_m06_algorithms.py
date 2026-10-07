import unittest
from exercises import m06_algorithms as m


class TestAlgorithms(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual(m.two_sum([2, 7, 11, 15], 9), (0, 1))
        self.assertEqual(m.two_sum([3, 2, 4], 6), (1, 2))
        self.assertIsNone(m.two_sum([1, 2], 10))

    def test_binary_search(self):
        nums = [1, 3, 5, 7, 9, 11]
        self.assertEqual(m.binary_search(nums, 7), 3)
        self.assertEqual(m.binary_search(nums, 1), 0)
        self.assertEqual(m.binary_search(nums, 4), -1)
        self.assertEqual(m.binary_search([], 1), -1)

    def test_is_balanced(self):
        self.assertTrue(m.is_balanced("{[()]}"))
        self.assertTrue(m.is_balanced(""))
        self.assertFalse(m.is_balanced("([)]"))
        self.assertFalse(m.is_balanced("(("))

    def test_fibonacci(self):
        self.assertEqual([m.fibonacci(i) for i in range(7)], [0, 1, 1, 2, 3, 5, 8])
        self.assertEqual(m.fibonacci(200), 280571172992510140037611932413038677189525)

    def test_most_frequent(self):
        self.assertEqual(m.most_frequent(["a", "b", "b", "a", "c"]), "a")
        self.assertEqual(m.most_frequent([1, 2, 2]), 2)

    def test_chunk(self):
        self.assertEqual(m.chunk([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])
        with self.assertRaises(ValueError):
            m.chunk([1], 0)
