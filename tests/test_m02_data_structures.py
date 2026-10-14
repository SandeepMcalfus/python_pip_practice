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

    # --- Lists ------------------------------------------------------------

    def test_rotate_list(self):
        self.assertEqual(m.rotate_list([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3])
        self.assertEqual(m.rotate_list([1, 2, 3], 4), [3, 1, 2])
        self.assertEqual(m.rotate_list([1, 2, 3], 0), [1, 2, 3])
        self.assertEqual(m.rotate_list([], 3), [])

    def test_chunk(self):
        self.assertEqual(m.chunk([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])
        self.assertEqual(m.chunk([1, 2, 3], 3), [[1, 2, 3]])
        self.assertEqual(m.chunk([], 2), [])

    def test_second_largest(self):
        self.assertEqual(m.second_largest([4, 1, 4, 3]), 3)
        self.assertEqual(m.second_largest([-1, -5]), -5)
        with self.assertRaises(ValueError):
            m.second_largest([7, 7])
        with self.assertRaises(ValueError):
            m.second_largest([])

    def test_running_total(self):
        self.assertEqual(m.running_total([1, 2, 3, 4]), [1, 3, 6, 10])
        self.assertEqual(m.running_total([]), [])

    def test_move_zeros_to_end(self):
        data = [0, 1, 0, 3, 12]
        self.assertEqual(m.move_zeros_to_end(data), [1, 3, 12, 0, 0])
        self.assertEqual(data, [0, 1, 0, 3, 12], "input list was modified")
        self.assertEqual(m.move_zeros_to_end([0, 0]), [0, 0])

    def test_find_all_indexes(self):
        self.assertEqual(m.find_all_indexes(["a", "b", "a"], "a"), [0, 2])
        self.assertEqual(m.find_all_indexes([1, 2, 3], 9), [])

    # --- Tuples -----------------------------------------------------------

    def test_min_max(self):
        self.assertEqual(m.min_max([3, 7, 1, 9]), (1, 9))
        self.assertEqual(m.min_max([5]), (5, 5))
        with self.assertRaises(ValueError):
            m.min_max([])

    def test_sort_by_second(self):
        self.assertEqual(m.sort_by_second([("a", 3), ("b", 1), ("c", 2)]),
                         [("b", 1), ("c", 2), ("a", 3)])

    def test_unzip_pairs(self):
        self.assertEqual(m.unzip_pairs([(1, "a"), (2, "b")]), ((1, 2), ("a", "b")))
        self.assertEqual(m.unzip_pairs([]), ((), ()))

    def test_count_coordinates(self):
        self.assertEqual(m.count_coordinates([(0, 0), (1, 2), (0, 0)]),
                         {(0, 0): 2, (1, 2): 1})

    # --- Dictionaries -----------------------------------------------------

    def test_invert_dict(self):
        self.assertEqual(m.invert_dict({"a": 1, "b": 2}), {1: "a", 2: "b"})
        self.assertEqual(m.invert_dict({}), {})

    def test_dict_from_lists(self):
        self.assertEqual(m.dict_from_lists(["a", "b"], [1, 2]), {"a": 1, "b": 2})
        self.assertEqual(m.dict_from_lists(["a", "b", "c"], [1]), {"a": 1})

    def test_filter_by_value(self):
        self.assertEqual(m.filter_by_value({"a": 5, "b": 2, "c": 9}, 5), {"a": 5, "c": 9})
        self.assertEqual(m.filter_by_value({"a": 1}, 10), {})

    def test_sort_dict_by_value(self):
        self.assertEqual(m.sort_dict_by_value({"x": 2, "y": 9, "z": 5}), ["y", "z", "x"])
        self.assertEqual(m.sort_dict_by_value({"a": 1, "b": 1, "c": 3}), ["c", "a", "b"])

    def test_top_n_words(self):
        self.assertEqual(m.top_n_words("a b a c b a", 2), [("a", 3), ("b", 2)])
        self.assertEqual(m.top_n_words("Dog cat dog", 1), [("dog", 2)])

    def test_safe_get(self):
        data = {"a": {"b": {"c": 1}}}
        self.assertEqual(m.safe_get(data, ["a", "b", "c"]), 1)
        self.assertEqual(m.safe_get(data, ["a", "b"]), {"c": 1})
        self.assertIsNone(m.safe_get(data, ["a", "x"]))
        self.assertEqual(m.safe_get(data, ["a", "b", "c", "d"], "nope"), "nope")

    def test_average_scores(self):
        self.assertEqual(m.average_scores({"ana": [90, 80], "bo": [70]}),
                         {"ana": 85.0, "bo": 70.0})
        self.assertEqual(m.average_scores({"cy": [1, 2, 2], "di": []}),
                         {"cy": 1.7, "di": 0.0})

    # --- Sets -------------------------------------------------------------

    def test_has_duplicates(self):
        self.assertTrue(m.has_duplicates([1, 2, 1]))
        self.assertFalse(m.has_duplicates([1, 2, 3]))
        self.assertFalse(m.has_duplicates([]))

    def test_only_in_one(self):
        self.assertEqual(m.only_in_one([1, 2, 3], [2, 3, 4]), [1, 4])
        self.assertEqual(m.only_in_one([1, 1], [1]), [])

    def test_missing_numbers(self):
        self.assertEqual(m.missing_numbers([1, 2, 4, 6], 6), [3, 5])
        self.assertEqual(m.missing_numbers([], 3), [1, 2, 3])

    def test_unique_letters(self):
        self.assertEqual(m.unique_letters(["Hi", "ho!"]), {"h", "i", "o"})
        self.assertEqual(m.unique_letters([]), set())

    # --- Comprehensions ---------------------------------------------------

    def test_squares_of_evens(self):
        self.assertEqual(m.squares_of_evens([1, 2, 3, 4]), [4, 16])
        self.assertEqual(m.squares_of_evens([1, 3]), [])

    def test_word_lengths(self):
        self.assertEqual(m.word_lengths(["hi", "cat"]), {"hi": 2, "cat": 3})

    def test_transpose(self):
        self.assertEqual(m.transpose([[1, 2, 3], [4, 5, 6]]), [[1, 4], [2, 5], [3, 6]])
        self.assertEqual(m.transpose([]), [])

    def test_pairs_that_sum(self):
        self.assertEqual(m.pairs_that_sum([1, 2, 3, 4], 5), [(0, 3), (1, 2)])
        self.assertEqual(m.pairs_that_sum([1, 1], 3), [])

    # --- Stacks & queues --------------------------------------------------

    def test_is_balanced(self):
        self.assertTrue(m.is_balanced("([]{})"))
        self.assertTrue(m.is_balanced("f(x[1]) + {y}"))
        self.assertTrue(m.is_balanced(""))
        self.assertFalse(m.is_balanced("([)]"))
        self.assertFalse(m.is_balanced("(("))
        self.assertFalse(m.is_balanced("))"))

    def test_last_n_items(self):
        self.assertEqual(m.last_n_items([1, 2, 3, 4, 5], 3), [3, 4, 5])
        self.assertEqual(m.last_n_items([1, 2], 5), [1, 2])

    def test_hot_potato(self):
        self.assertEqual(m.hot_potato(["A", "B", "C", "D"], 2), "A")
        self.assertEqual(m.hot_potato(["solo"], 3), "solo")

    # --- collections ------------------------------------------------------

    def test_first_unique_char(self):
        self.assertEqual(m.first_unique_char("leetcode"), 0)
        self.assertEqual(m.first_unique_char("loveleetcode"), 2)
        self.assertEqual(m.first_unique_char("aabb"), -1)

    def test_group_anagrams(self):
        self.assertEqual(m.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
                         [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])
        self.assertEqual(m.group_anagrams([]), [])

    def test_make_point(self):
        p = m.make_point(3, 4)
        self.assertEqual((p.x, p.y), (3, 4))
        self.assertEqual(p, (3, 4))
        self.assertEqual(type(p).__name__, "Point")
        with self.assertRaises(AttributeError):
            p.x = 10
