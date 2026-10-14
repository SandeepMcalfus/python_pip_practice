"""
Module 3 - Functions & Error Handling: defaults, *args/**kwargs, lambdas,
exceptions, decorators.
"""
import functools


def safe_divide(a, b, default=None):
    """Return a / b. If b is 0 return `default`. If either value is not a number
    (int/float), raise TypeError."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a and b must be numbers")
    if b == 0:
        return default
    return a / b


def total(*numbers) -> float:
    """Sum any number of arguments.  total(1, 2, 3) -> 6;  total() -> 0"""
    return sum(numbers)


def build_profile(name: str, **details) -> dict:
    """build_profile("Asha", age=30, city="Pune") -> {"name": "Asha", "age": 30, "city": "Pune"}"""
    profile = {"name": name}
    profile.update(details)
    return profile


def parse_int_list(text: str) -> list:
    """Parse "1, 2, x, 4" -> [1, 2, 4]. Skip anything that can't become an int.
    Use try/except ValueError (don't use isdigit)."""
    result = []
    for part in text.split(","):
        try:
            result.append(int(part))
        except ValueError:
            continue
    return result


def sort_by_age(people: list) -> list:
    """people is a list of dicts like {"name": "A", "age": 30}.
    Return a new list sorted by age (youngest first). Use sorted() with a lambda key."""
    return sorted(people, key=lambda person: person["age"])


def count_calls(func):
    """Decorator: wrap func so that wrapper.calls holds how many times it was called.

        @count_calls
        def hello(): return "hi"
        hello(); hello()
        hello.calls -> 2

    The wrapper must still return func's result and pass through all arguments.
    Bonus: use functools.wraps so hello.__name__ stays "hello"."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


# ---------------------------------------------------------------------------
# Default & keyword arguments  (defaults, keyword-only args, the mutable-default trap)
# ---------------------------------------------------------------------------

def greet(name: str, greeting: str = "Hello", punctuation: str = "!") -> str:
    """greet("Asha") -> "Hello, Asha!"     greet("Asha", "Hi") -> "Hi, Asha!"
    greet("Asha", punctuation=".") -> "Hello, Asha." """
    return f"{greeting}, {name}{punctuation}"


def append_item(item, items=None) -> list:
    """Append item to items and return the list. If items is not given, start a NEW list.
    append_item(1) -> [1], then append_item(2) -> [2]   (NOT [1, 2]!)
    Hint: never use a mutable default like items=[] -- use None and create the list inside."""
    if items is None:
        items = []
    items.append(item)
    return items


def describe_person(name: str, *, age: int, city: str = "unknown") -> str:
    """age and city are KEYWORD-ONLY (everything after the bare * must be named).
    describe_person("Asha", age=30, city="Pune") -> "Asha, 30, Pune"
    describe_person("Bo", age=5) -> "Bo, 5, unknown" """
    return f"{name}, {age}, {city}"


def make_tag(text: str, tag: str = "p", **attrs) -> str:
    """Build an HTML tag; keyword arguments become attributes, in the order given.
    make_tag("hi") -> "<p>hi</p>"
    make_tag("go", "a", href="/home") -> '<a href="/home">go</a>' """
    attributes = ""
    for key, value in attrs.items():
        attributes += f' {key}="{value}"'
    return f"<{tag}{attributes}>{text}</{tag}>"


# ---------------------------------------------------------------------------
# *args and **kwargs
# ---------------------------------------------------------------------------

def average(*numbers) -> float:
    """Average of any number of arguments.  average(1, 2, 3) -> 2.0;  average() -> 0.0"""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def longest(*words) -> str:
    """Longest of the given words; on a tie the first one.  longest() -> "" """
    best = ""
    for word in words:
        if len(word) > len(best):
            best = word
    return best


def merge_settings(defaults: dict, **overrides) -> dict:
    """Return a NEW dict: defaults updated with the keyword arguments.
    merge_settings({"theme": "light", "size": 12}, size=14) -> {"theme": "light", "size": 14}
    Do not modify `defaults`."""
    result = dict(defaults)
    result.update(overrides)
    return result


def format_call(func_name: str, *args, **kwargs) -> str:
    """Show how a call would look. Use repr() for every value.
    format_call("add", 1, 2, b=3) -> "add(1, 2, b=3)"
    format_call("greet", "Asha")  -> "greet('Asha')"
    format_call("f")              -> "f()" """
    parts = [repr(arg) for arg in args]
    parts += [f"{key}={value!r}" for key, value in kwargs.items()]
    return f"{func_name}({', '.join(parts)})"


# ---------------------------------------------------------------------------
# Functions as values  (lambdas, higher-order functions, closures, nonlocal)
# ---------------------------------------------------------------------------

def apply_n_times(func, value, n: int):
    """Call func on value n times, feeding each result back in.
    apply_n_times(lambda x: x * 2, 1, 3) -> 8;   n = 0 -> value unchanged."""
    for _ in range(n):
        value = func(value)
    return value


def compose(f, g):
    """Return a NEW function that computes f(g(x)).
    add_one_after_double = compose(lambda x: x + 1, lambda x: x * 2)
    add_one_after_double(5) -> 11"""
    def composed(x):
        return f(g(x))
    return composed


def pipeline(value, *funcs):
    """Pass value through each function in order.
    pipeline(3, lambda x: x + 1, lambda x: x * 10) -> 40;   pipeline(3) -> 3"""
    for func in funcs:
        value = func(value)
    return value


def make_multiplier(n):
    """Return a function that multiplies its argument by n (a closure).
    triple = make_multiplier(3);  triple(5) -> 15"""
    def multiply(x):
        return x * n
    return multiply


def make_counter():
    """Return a function that returns 1, 2, 3, ... on each call.
    Every counter made by make_counter() counts on its own.
    Hint: a variable in make_counter plus `nonlocal` in the inner function."""
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


def sort_by_last_char(words: list) -> list:
    """Sort words by their LAST character (use a lambda key). Ties keep the original order.
    ["apple", "kiwi", "banana"] -> ["banana", "apple", "kiwi"]"""
    return sorted(words, key=lambda word: word[-1])


# ---------------------------------------------------------------------------
# Recursion  (no loops in this section!)
# ---------------------------------------------------------------------------

def recursive_sum(numbers: list) -> int:
    """Sum a list using recursion (no loops, no sum()).  [1, 2, 3] -> 6,  [] -> 0
    Hint: first item + recursive_sum(the rest)."""
    if not numbers:
        return 0
    return numbers[0] + recursive_sum(numbers[1:])


def flatten_deep(nested: list) -> list:
    """Flatten ANY depth of nesting.  [1, [2, [3, [4]]], 5] -> [1, 2, 3, 4, 5]
    Hint: isinstance(item, list)."""
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten_deep(item))
        else:
            result.append(item)
    return result


def power(base, exponent: int):
    """base ** exponent using recursion (exponent >= 0).  power(2, 10) -> 1024,  power(5, 0) -> 1"""
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)


def to_binary(n: int) -> str:
    """Binary string of a non-negative int using recursion (not bin()).
    10 -> "1010",  1 -> "1",  0 -> "0"
    Hint: to_binary(n // 2) + str(n % 2)."""
    if n < 2:
        return str(n)
    return to_binary(n // 2) + str(n % 2)


# ---------------------------------------------------------------------------
# Exceptions  (try/except/else/finally, raise, custom exceptions)
# ---------------------------------------------------------------------------

class InsufficientFundsError(Exception):
    """A custom exception -- this is all it takes to make one. Used by withdraw()."""


def safe_int(text, default: int = 0) -> int:
    """int(text), or default if it can't be converted.
    "42" -> 42,  "abc" -> 0,  None -> 0
    Hint: int(None) raises TypeError, int("abc") raises ValueError -- catch both."""
    try:
        return int(text)
    except (TypeError, ValueError):
        return default


def validate_age(age) -> int:
    """Return age if it is valid.
    Raise TypeError if age is not an int, ValueError if it is below 0 or above 150."""
    if not isinstance(age, int):
        raise TypeError(f"age must be an int, got {type(age).__name__}")
    if age < 0 or age > 150:
        raise ValueError(f"age must be between 0 and 150, got {age}")
    return age


def withdraw(balance: float, amount: float) -> float:
    """Return the new balance.
    Raise ValueError if amount <= 0.
    Raise InsufficientFundsError (defined above) if amount > balance."""
    if amount <= 0:
        raise ValueError(f"amount must be positive, got {amount}")
    if amount > balance:
        raise InsufficientFundsError(f"cannot withdraw {amount}, balance is {balance}")
    return balance - amount


def try_all(funcs: list) -> list:
    """Call each zero-argument function. Collect its result, or the NAME of the
    exception it raised.
    [lambda: 1, lambda: 1 / 0, lambda: int("x")] -> [1, "ZeroDivisionError", "ValueError"]
    Hint: except Exception as e:  ...  type(e).__name__"""
    results = []
    for func in funcs:
        try:
            results.append(func())
        except Exception as e:
            results.append(type(e).__name__)
    return results


def retry(func, attempts: int):
    """Call func() until it succeeds, at most `attempts` times, and return its result.
    If every attempt fails, re-raise the LAST exception."""
    last_error = None
    for _ in range(attempts):
        try:
            return func()
        except Exception as e:
            last_error = e
    raise last_error


def run_with_cleanup(func, log: list):
    """Append "start" to log, then call func().
    On success append "ok" and return the result.
    On any exception append "error" and return None.
    ALWAYS append "cleanup" at the very end.   Hint: try/except/finally."""
    log.append("start")
    try:
        result = func()
        log.append("ok")
        return result
    except Exception:
        log.append("error")
        return None
    finally:
        log.append("cleanup")


# ---------------------------------------------------------------------------
# Decorators  (wrappers, functools.wraps, decorators that take arguments)
# ---------------------------------------------------------------------------

def uppercase(func):
    """Decorator: upper-case whatever string func returns. Keep func's __name__.
        @uppercase
        def hi(name): return f"hi {name}"
        hi("bo") -> "HI BO" """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper


def memoize(func):
    """Decorator: remember results by positional arguments so func runs once per input.
    Expose the dict as wrapper.cache, e.g. {(5,): 120}."""
    @functools.wraps(func)
    def wrapper(*args):
        if args not in wrapper.cache:
            wrapper.cache[args] = func(*args)
        return wrapper.cache[args]

    wrapper.cache = {}
    return wrapper


def repeat(times: int):
    """Decorator FACTORY: @repeat(3) calls the function 3 times and returns a list of results.
        @repeat(3)
        def hi(): return "hi"
        hi() -> ["hi", "hi", "hi"]
    Hint: three levels -- repeat(times) returns decorator(func) returns wrapper(*args, **kwargs)."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return [func(*args, **kwargs) for _ in range(times)]
        return wrapper
    return decorator


def only_positive(func):
    """Decorator: raise ValueError if ANY argument (positional or keyword) is a negative number.
    Otherwise call func normally."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for value in list(args) + list(kwargs.values()):
            if isinstance(value, (int, float)) and value < 0:
                raise ValueError(f"negative value not allowed: {value}")
        return func(*args, **kwargs)
    return wrapper


# ---------------------------------------------------------------------------
# Generators  (yield)
# ---------------------------------------------------------------------------

def countdown(n: int):
    """Generator: yield n, n-1, ..., 1.   list(countdown(3)) -> [3, 2, 1]
    Use `yield` (don't build a list)."""
    while n > 0:
        yield n
        n -= 1


def evens_up_to(limit: int):
    """Generator: yield the even numbers from 0 up to and including limit.
    list(evens_up_to(8)) -> [0, 2, 4, 6, 8]"""
    for number in range(0, limit + 1, 2):
        yield number
