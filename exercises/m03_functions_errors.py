"""
Module 3 - Functions & Error Handling: defaults, *args/**kwargs, lambdas,
exceptions, decorators.
"""


def safe_divide(a, b, default=None):
    """Return a / b. If b is 0 return `default`. If either value is not a number
    (int/float), raise TypeError."""
    raise NotImplementedError


def total(*numbers) -> float:
    """Sum any number of arguments.  total(1, 2, 3) -> 6;  total() -> 0"""
    raise NotImplementedError


def build_profile(name: str, **details) -> dict:
    """build_profile("Asha", age=30, city="Pune") -> {"name": "Asha", "age": 30, "city": "Pune"}"""
    raise NotImplementedError


def parse_int_list(text: str) -> list:
    """Parse "1, 2, x, 4" -> [1, 2, 4]. Skip anything that can't become an int.
    Use try/except ValueError (don't use isdigit)."""
    raise NotImplementedError


def sort_by_age(people: list) -> list:
    """people is a list of dicts like {"name": "A", "age": 30}.
    Return a new list sorted by age (youngest first). Use sorted() with a lambda key."""
    raise NotImplementedError


def count_calls(func):
    """Decorator: wrap func so that wrapper.calls holds how many times it was called.

        @count_calls
        def hello(): return "hi"
        hello(); hello()
        hello.calls -> 2

    The wrapper must still return func's result and pass through all arguments.
    Bonus: use functools.wraps so hello.__name__ stays "hello"."""
    raise NotImplementedError
