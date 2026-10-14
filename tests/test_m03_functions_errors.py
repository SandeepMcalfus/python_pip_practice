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

    # --- Default & keyword arguments --------------------------------------

    def test_greet(self):
        self.assertEqual(m.greet("Asha"), "Hello, Asha!")
        self.assertEqual(m.greet("Asha", "Hi"), "Hi, Asha!")
        self.assertEqual(m.greet("Asha", punctuation="."), "Hello, Asha.")

    def test_append_item(self):
        self.assertEqual(m.append_item(1), [1])
        self.assertEqual(m.append_item(2), [2], "the default list is being shared between calls")
        existing = [0]
        self.assertIs(m.append_item(1, existing), existing)
        self.assertEqual(existing, [0, 1])

    def test_describe_person(self):
        self.assertEqual(m.describe_person("Asha", age=30, city="Pune"), "Asha, 30, Pune")
        self.assertEqual(m.describe_person("Bo", age=5), "Bo, 5, unknown")
        with self.assertRaises(TypeError):
            m.describe_person("Bo", 5)

    def test_make_tag(self):
        self.assertEqual(m.make_tag("hi"), "<p>hi</p>")
        self.assertEqual(m.make_tag("go", "a", href="/home"), '<a href="/home">go</a>')
        self.assertEqual(m.make_tag("x", "div", id="main", title="t"),
                         '<div id="main" title="t">x</div>')

    # --- *args and **kwargs -----------------------------------------------

    def test_average(self):
        self.assertEqual(m.average(1, 2, 3), 2.0)
        self.assertEqual(m.average(5), 5.0)
        self.assertEqual(m.average(), 0.0)

    def test_longest(self):
        self.assertEqual(m.longest("hi", "hello", "hey"), "hello")
        self.assertEqual(m.longest("ab", "cd"), "ab")
        self.assertEqual(m.longest(), "")

    def test_merge_settings(self):
        defaults = {"theme": "light", "size": 12}
        self.assertEqual(m.merge_settings(defaults, size=14, bold=True),
                         {"theme": "light", "size": 14, "bold": True})
        self.assertEqual(defaults, {"theme": "light", "size": 12}, "defaults was modified")

    def test_format_call(self):
        self.assertEqual(m.format_call("add", 1, 2, b=3), "add(1, 2, b=3)")
        self.assertEqual(m.format_call("greet", "Asha"), "greet('Asha')")
        self.assertEqual(m.format_call("f"), "f()")
        self.assertEqual(m.format_call("g", x=None), "g(x=None)")

    # --- Functions as values ----------------------------------------------

    def test_apply_n_times(self):
        self.assertEqual(m.apply_n_times(lambda x: x * 2, 1, 3), 8)
        self.assertEqual(m.apply_n_times(lambda s: s + "!", "hi", 2), "hi!!")
        self.assertEqual(m.apply_n_times(lambda x: x * 2, 7, 0), 7)

    def test_compose(self):
        f = m.compose(lambda x: x + 1, lambda x: x * 2)
        self.assertEqual(f(5), 11)
        g = m.compose(str.upper, str.strip)
        self.assertEqual(g("  hi "), "HI")

    def test_pipeline(self):
        self.assertEqual(m.pipeline(3, lambda x: x + 1, lambda x: x * 10), 40)
        self.assertEqual(m.pipeline(3, lambda x: x * 10, lambda x: x + 1), 31)
        self.assertEqual(m.pipeline(3), 3)

    def test_make_multiplier(self):
        triple = m.make_multiplier(3)
        double = m.make_multiplier(2)
        self.assertEqual(triple(5), 15)
        self.assertEqual(double(5), 10)

    def test_make_counter(self):
        c1 = m.make_counter()
        self.assertEqual([c1(), c1(), c1()], [1, 2, 3])
        c2 = m.make_counter()
        self.assertEqual(c2(), 1)
        self.assertEqual(c1(), 4)

    def test_sort_by_last_char(self):
        self.assertEqual(m.sort_by_last_char(["apple", "kiwi", "banana"]),
                         ["banana", "apple", "kiwi"])
        self.assertEqual(m.sort_by_last_char(["ba", "aa"]), ["ba", "aa"])

    # --- Recursion --------------------------------------------------------

    def test_recursive_sum(self):
        self.assertEqual(m.recursive_sum([1, 2, 3]), 6)
        self.assertEqual(m.recursive_sum([]), 0)

    def test_flatten_deep(self):
        self.assertEqual(m.flatten_deep([1, [2, [3, [4]]], 5]), [1, 2, 3, 4, 5])
        self.assertEqual(m.flatten_deep([[], [[]]]), [])
        self.assertEqual(m.flatten_deep([]), [])

    def test_power(self):
        self.assertEqual(m.power(2, 10), 1024)
        self.assertEqual(m.power(5, 0), 1)
        self.assertEqual(m.power(3, 3), 27)

    def test_to_binary(self):
        self.assertEqual(m.to_binary(10), "1010")
        self.assertEqual(m.to_binary(1), "1")
        self.assertEqual(m.to_binary(0), "0")
        self.assertEqual(m.to_binary(255), "11111111")

    # --- Exceptions -------------------------------------------------------

    def test_safe_int(self):
        self.assertEqual(m.safe_int("42"), 42)
        self.assertEqual(m.safe_int("abc"), 0)
        self.assertEqual(m.safe_int("abc", -1), -1)
        self.assertEqual(m.safe_int(None), 0)

    def test_validate_age(self):
        self.assertEqual(m.validate_age(30), 30)
        self.assertEqual(m.validate_age(0), 0)
        with self.assertRaises(TypeError):
            m.validate_age("30")
        with self.assertRaises(ValueError):
            m.validate_age(-1)
        with self.assertRaises(ValueError):
            m.validate_age(151)

    def test_withdraw(self):
        self.assertTrue(issubclass(m.InsufficientFundsError, Exception))
        self.assertEqual(m.withdraw(100, 30), 70)
        self.assertEqual(m.withdraw(50, 50), 0)
        with self.assertRaises(m.InsufficientFundsError):
            m.withdraw(10, 20)
        with self.assertRaises(ValueError):
            m.withdraw(10, 0)

    def test_try_all(self):
        funcs = [lambda: 1, lambda: 1 / 0, lambda: int("x"), lambda: {}["k"]]
        self.assertEqual(m.try_all(funcs), [1, "ZeroDivisionError", "ValueError", "KeyError"])
        self.assertEqual(m.try_all([]), [])

    def test_retry(self):
        calls = []

        def flaky():
            calls.append(1)
            if len(calls) < 3:
                raise ConnectionError("try again")
            return "ok"

        self.assertEqual(m.retry(flaky, 5), "ok")
        self.assertEqual(len(calls), 3)

        attempts = []

        def always_fails():
            attempts.append(1)
            raise ValueError(f"attempt {len(attempts)}")

        with self.assertRaises(ValueError) as ctx:
            m.retry(always_fails, 2)
        self.assertEqual(len(attempts), 2)
        self.assertEqual(str(ctx.exception), "attempt 2")

    def test_run_with_cleanup(self):
        log = []
        self.assertEqual(m.run_with_cleanup(lambda: 42, log), 42)
        self.assertEqual(log, ["start", "ok", "cleanup"])
        log = []
        self.assertIsNone(m.run_with_cleanup(lambda: 1 / 0, log))
        self.assertEqual(log, ["start", "error", "cleanup"])

    # --- Decorators -------------------------------------------------------

    def test_uppercase(self):
        @m.uppercase
        def hi(name):
            return f"hi {name}"
        self.assertEqual(hi("bo"), "HI BO")
        self.assertEqual(hi.__name__, "hi")

    def test_memoize(self):
        real_calls = []

        @m.memoize
        def square(n):
            real_calls.append(n)
            return n * n

        self.assertEqual(square(4), 16)
        self.assertEqual(square(4), 16)
        self.assertEqual(square(5), 25)
        self.assertEqual(real_calls, [4, 5])
        self.assertEqual(square.cache, {(4,): 16, (5,): 25})

    def test_repeat(self):
        @m.repeat(3)
        def hi():
            return "hi"
        self.assertEqual(hi(), ["hi", "hi", "hi"])

        @m.repeat(2)
        def add(a, b=0):
            return a + b
        self.assertEqual(add(1, b=2), [3, 3])

    def test_only_positive(self):
        @m.only_positive
        def area(w, h):
            return w * h
        self.assertEqual(area(2, 3), 6)
        self.assertEqual(area(0, h=4), 0)
        with self.assertRaises(ValueError):
            area(-1, 3)
        with self.assertRaises(ValueError):
            area(2, h=-3)

    # --- Generators -------------------------------------------------------

    def test_countdown(self):
        import inspect
        gen = m.countdown(3)
        self.assertTrue(inspect.isgenerator(gen), "countdown should use yield")
        self.assertEqual(list(gen), [3, 2, 1])
        self.assertEqual(list(m.countdown(0)), [])

    def test_evens_up_to(self):
        import inspect
        self.assertTrue(inspect.isgenerator(m.evens_up_to(4)), "evens_up_to should use yield")
        self.assertEqual(list(m.evens_up_to(8)), [0, 2, 4, 6, 8])
        self.assertEqual(list(m.evens_up_to(7)), [0, 2, 4, 6])
        self.assertEqual(list(m.evens_up_to(0)), [0])
