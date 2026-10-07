import unittest
from exercises import m03_functions_errors as m


class TestFunctionsErrors(unittest.TestCase):
    def test_safe_divide(self):
        self.assertEqual(m.safe_divide(10, 2), 5)
        self.assertIsNone(m.safe_divide(1, 0))
        self.assertEqual(m.safe_divide(1, 0, default=0), 0)
        with self.assertRaises(TypeError):
            m.safe_divide("10", 2)

    def test_total(self):
        self.assertEqual(m.total(1, 2, 3), 6)
        self.assertEqual(m.total(), 0)

    def test_build_profile(self):
        self.assertEqual(m.build_profile("Asha", age=30, city="Pune"),
                         {"name": "Asha", "age": 30, "city": "Pune"})

    def test_parse_int_list(self):
        self.assertEqual(m.parse_int_list("1, 2, x, 4"), [1, 2, 4])
        self.assertEqual(m.parse_int_list("-3, 7"), [-3, 7])

    def test_sort_by_age(self):
        people = [{"name": "A", "age": 40}, {"name": "B", "age": 25}]
        self.assertEqual([p["name"] for p in m.sort_by_age(people)], ["B", "A"])
        self.assertEqual(people[0]["name"], "A", "original list was modified")

    def test_count_calls(self):
        @m.count_calls
        def add(a, b=0):
            return a + b
        self.assertEqual(add(2, b=3), 5)
        add(1)
        self.assertEqual(add.calls, 2)
        self.assertEqual(add.__name__, "add")
