import unittest
from exercises import m02_data_structures as m


class TestDataStructures(unittest.TestCase):
    def test_remove_duplicates(self):
        self.assertEqual(m.remove_duplicates([3, 1, 3, 2, 1]), [3, 1, 2])
        self.assertEqual(m.remove_duplicates([]), [])

    def test_word_frequency(self):
        self.assertEqual(m.word_frequency("the cat and The hat"),
                         {"the": 2, "cat": 1, "and": 1, "hat": 1})

    def test_merge_dicts(self):
        a, b = {"x": 1, "y": 2}, {"y": 3, "z": 4}
        self.assertEqual(m.merge_dicts(a, b), {"x": 1, "y": 5, "z": 4})
        self.assertEqual(a, {"x": 1, "y": 2}, "input dict was modified")

    def test_common_elements(self):
        self.assertEqual(m.common_elements([5, 1, 2, 2, 3], [3, 2, 9, 5]), [2, 3, 5])
        self.assertEqual(m.common_elements([1], [2]), [])

    def test_flatten(self):
        self.assertEqual(m.flatten([[1, 2], [3], [], [4, 5]]), [1, 2, 3, 4, 5])

    def test_group_by_length(self):
        self.assertEqual(m.group_by_length(["hi", "cat", "yo"]),
                         {2: ["hi", "yo"], 3: ["cat"]})
