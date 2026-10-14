"""
Module 4 - Object-Oriented Programming: classes, properties, inheritance,
dunder methods.
"""
import functools
import json
import math
from abc import ABC, abstractmethod
from dataclasses import dataclass


class InsufficientFundsError(Exception):
    """Raised when a withdrawal is larger than the balance. (Already done for you.)"""


class BankAccount:
    """
    - BankAccount(owner, balance=0)
    - .owner, .balance attributes
    - deposit(amount): amount must be > 0 else raise ValueError
    - withdraw(amount): amount must be > 0 else ValueError;
      if amount > balance raise InsufficientFundsError
    - .history: list of tuples like ("deposit", 100) / ("withdraw", 40)
    - str(account) -> "Asha: 60.00"  (2 decimal places)
    """

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError(f"deposit must be positive, got {amount}")
        self.balance += amount
        self.history.append(("deposit", amount))

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError(f"withdrawal must be positive, got {amount}")
        if amount > self.balance:
            raise InsufficientFundsError(f"cannot withdraw {amount}, balance is {self.balance}")
        self.balance -= amount
        self.history.append(("withdraw", amount))

    def __str__(self):
        return f"{self.owner}: {self.balance:.2f}"


class SavingsAccount(BankAccount):
    """
    Inherits from BankAccount.
    - SavingsAccount(owner, balance=0, rate=0.05)
    - add_interest(): deposits balance * rate (and records it in history as a deposit)
    """

    def __init__(self, owner, balance=0, rate=0.05):
        super().__init__(owner, balance)
        self.rate = rate

    def add_interest(self):
        self.deposit(self.balance * self.rate)


class Rectangle:
    """
    - Rectangle(width, height); both must be > 0 else ValueError
    - .area property and .perimeter property (not methods!)
    - Two rectangles are equal (==) if width and height match
    - Rectangles can be sorted by area (implement __lt__)
    """

    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("width and height must be positive")
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)

    def __eq__(self, other):
        return self.width == other.width and self.height == other.height

    def __lt__(self, other):
        return self.area < other.area


# ---------------------------------------------------------------------------
# Classes & instances  (__init__, self, instance attributes, methods)
# ---------------------------------------------------------------------------

class Person:
    """
    - Person(name, age) with .name and .age attributes
    - greet() -> "Hi, I'm Asha"
    - have_birthday(): add 1 to age and RETURN the new age
    - is_adult() -> True if age >= 18
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name}"

    def have_birthday(self):
        self.age += 1
        return self.age

    def is_adult(self):
        return self.age >= 18


class ClickCounter:
    """
    - ClickCounter(start=0); current count in .value
    - increment(step=1) and decrement(step=1) both RETURN self, so calls chain:
          ClickCounter().increment().increment(5).value -> 6
    - decrement never goes below 0
    - reset() sets value back to the original start
    """

    def __init__(self, start=0):
        self.start = start
        self.value = start

    def increment(self, step=1):
        self.value += step
        return self

    def decrement(self, step=1):
        self.value = max(0, self.value - step)
        return self

    def reset(self):
        self.value = self.start


# ---------------------------------------------------------------------------
# Properties & validation  (@property, setters, read-only attributes)
# ---------------------------------------------------------------------------

class Temperature:
    """
    - Temperature(celsius)
    - .celsius property WITH a setter; setting below -273.15 raises ValueError
      (the check must also apply in __init__ -- hint: assign through the property)
    - .fahrenheit property WITH a setter (F = C * 9/5 + 32); setting it updates celsius
    - @classmethod from_fahrenheit(f) -> a new Temperature
    """

    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError(f"temperature below absolute zero: {value}")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5 / 9

    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        return cls((fahrenheit - 32) * 5 / 9)


class Circle:
    """
    - Circle(radius); .radius property, setter raises ValueError if radius <= 0
    - .area property (use math.pi) -- read-only
    - .diameter property WITH a setter: c.diameter = 10 makes radius 5
    """

    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError(f"radius must be positive, got {value}")
        self._radius = value

    @property
    def area(self):
        return math.pi * self._radius ** 2

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2


class User:
    """
    - User(username, password); password must be at least 8 chars else ValueError
    - store the password in a "private" attribute (self._password)
    - check_password(attempt) -> bool
    - change_password(old, new): wrong old password -> PermissionError;
      new password follows the same 8-char rule
    - str(user) and repr(user) -> "User(asha)" -- NEVER include the password
    """

    def __init__(self, username, password):
        self.username = username
        self._set_password(password)

    def _set_password(self, password):
        if len(password) < 8:
            raise ValueError("password must be at least 8 characters")
        self._password = password

    def check_password(self, attempt):
        return attempt == self._password

    def change_password(self, old, new):
        if not self.check_password(old):
            raise PermissionError("old password is incorrect")
        self._set_password(new)

    def __repr__(self):
        return f"User({self.username})"


# ---------------------------------------------------------------------------
# Class attributes, @classmethod and @staticmethod
# ---------------------------------------------------------------------------

class Employee:
    """
    - Class attributes: raise_amount = 1.05 and count = 0
    - Employee(name, salary); every new Employee adds 1 to Employee.count
    - apply_raise(): salary = salary * self.raise_amount
      (setting e.raise_amount on ONE employee must not change the others)
    - @classmethod from_string("Asha-50000") -> Employee("Asha", 50000)  (salary as int)
    - @staticmethod is_workday(day_index) -> True for 0..4 (Mon..Fri), False for 5, 6
    """

    raise_amount = 1.05
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def apply_raise(self):
        self.salary = self.salary * self.raise_amount

    @classmethod
    def from_string(cls, text):
        name, salary = text.split("-")
        return cls(name, int(salary))

    @staticmethod
    def is_workday(day_index):
        return 0 <= day_index <= 4


# ---------------------------------------------------------------------------
# Inheritance & polymorphism  (super(), overriding, isinstance)
# ---------------------------------------------------------------------------

class Animal:
    """
    - Animal(name, sound)
    - speak() -> "Rex says Woof"
    """

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}"


class Dog(Animal):
    """
    - Dog(name) -- calls super().__init__ with sound "Woof"
    - fetch() -> "Rex fetches the ball"
    """

    def __init__(self, name):
        super().__init__(name, "Woof")

    def fetch(self):
        return f"{self.name} fetches the ball"


class Cat(Animal):
    """
    - Cat(name) -- sound "Meow"
    - OVERRIDE speak() to add " (if it feels like it)" to the parent's result:
          Cat("Tom").speak() -> "Tom says Meow (if it feels like it)"
      Hint: super().speak()
    """

    def __init__(self, name):
        super().__init__(name, "Meow")

    def speak(self):
        return super().speak() + " (if it feels like it)"


class Shape:
    """Base class.  area() must be overridden by subclasses (already done for you).
    - describe() -> "Square with area 4.00"   (hint: type(self).__name__)"""

    def area(self):
        raise NotImplementedError("subclasses must implement area()")

    def describe(self):
        return f"{type(self).__name__} with area {self.area():.2f}"


class Square(Shape):
    """Square(side); area() -> side * side"""

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Triangle(Shape):
    """Triangle(base, height); area() -> 0.5 * base * height"""

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


def total_area(shapes: list) -> float:
    """Sum of area() for any mix of shapes -- polymorphism in action."""
    return sum(shape.area() for shape in shapes)


# ---------------------------------------------------------------------------
# Abstract base classes & mixins  (abc.ABC, @abstractmethod, vars())
# ---------------------------------------------------------------------------

class PaymentMethod(ABC):
    """
    Make this an ABSTRACT class: inherit from abc.ABC and mark pay() with @abstractmethod.
    - PaymentMethod() itself must raise TypeError
    - a subclass that doesn't implement pay() must also raise TypeError when created
    """

    @abstractmethod
    def pay(self, amount):
        """Charge `amount` and return a description of the payment."""


class CreditCard(PaymentMethod):
    """
    - CreditCard(card_number)
    - pay(50) -> "Paid 50.00 with card ending 5678"  (last 4 digits)
    """

    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        return f"Paid {amount:.2f} with card ending {self.card_number[-4:]}"


class PayPal(PaymentMethod):
    """
    - PayPal(email)
    - pay(50) -> "Paid 50.00 via PayPal (asha@example.com)"
    """

    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        return f"Paid {amount:.2f} via PayPal ({self.email})"


class ToDictMixin:
    """A mixin adds behaviour to any class that inherits it.
    - to_dict() -> a COPY of the object's attributes (hint: vars(self))
    - to_json() -> json.dumps(self.to_dict(), sort_keys=True)"""

    def to_dict(self):
        return dict(vars(self))

    def to_json(self):
        return json.dumps(self.to_dict(), sort_keys=True)


class Product(ToDictMixin):
    """
    - Product(name, price, quantity=0); price < 0 raises ValueError
    - .total_value property -> price * quantity
    - Product("pen", 1.5, 4).to_json() -> '{"name": "pen", "price": 1.5, "quantity": 4}'
    """

    def __init__(self, name, price, quantity=0):
        if price < 0:
            raise ValueError(f"price cannot be negative, got {price}")
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def total_value(self):
        return self.price * self.quantity


# ---------------------------------------------------------------------------
# Dunder (magic) methods  (__repr__, __eq__, __add__, __len__, __getitem__ ...)
# ---------------------------------------------------------------------------

class Vector:
    """
    - Vector(x, y)
    - v1 + v2, v1 - v2         -> new Vector
    - v * 3 AND 3 * v          -> new Vector   (hint: __mul__ and __rmul__)
    - v1 == v2                 -> compares x and y
    - abs(v)                   -> length, e.g. abs(Vector(3, 4)) -> 5.0
    - bool(v)                  -> False only for Vector(0, 0)
    - repr(v)                  -> "Vector(1, 2)"
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return self * scalar

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


@functools.total_ordering
class Money:
    """
    - Money(amount, currency="USD")
    - str(m) -> "10.50 USD"
    - m1 + m2 -> new Money; different currencies raise ValueError
    - ==, <, <=, >, >= all work for the same currency (comparing different currencies
      raises ValueError).  Hint: write __eq__ and __lt__, then use @functools.total_ordering
    """

    def __init__(self, amount, currency="USD"):
        self.amount = round(amount, 2)
        self.currency = currency

    def _check_currency(self, other):
        if self.currency != other.currency:
            raise ValueError(f"cannot mix {self.currency} and {other.currency}")

    def __add__(self, other):
        self._check_currency(other)
        return Money(self.amount + other.amount, self.currency)

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency

    def __lt__(self, other):
        self._check_currency(other)
        return self.amount < other.amount

    def __str__(self):
        return f"{self.amount:.2f} {self.currency}"


class Fraction:
    """
    - Fraction(numerator, denominator=1); denominator 0 raises ZeroDivisionError
    - always stored in lowest terms with a positive denominator:
          Fraction(2, 4) -> 1/2,   Fraction(1, -2) -> -1/2      (hint: math.gcd)
    - str(f) -> "1/2", or just "3" when the denominator is 1
    - f1 + f2, f1 * f2 -> new Fraction;  f1 == f2;  float(f) -> 0.5
    """

    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError("denominator cannot be 0")
        if denominator < 0:
            numerator, denominator = -numerator, -denominator
        divisor = math.gcd(numerator, denominator)
        self.numerator = numerator // divisor
        self.denominator = denominator // divisor

    def __add__(self, other):
        return Fraction(self.numerator * other.denominator + other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator,
                        self.denominator * other.denominator)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __float__(self):
        return self.numerator / self.denominator

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"


class Playlist:
    """Make a Playlist behave like a sequence.
    - Playlist(name); add(song)
    - len(p), p[0], p[-1], p[1:3] (a list), "song" in p, and `for song in p` all work
    """

    def __init__(self, name):
        self.name = name
        self.songs = []

    def add(self, song):
        self.songs.append(song)

    def __len__(self):
        return len(self.songs)

    def __getitem__(self, index):
        return self.songs[index]

    def __contains__(self, song):
        return song in self.songs

    def __iter__(self):
        return iter(self.songs)


class Stack:
    """
    - push(item), pop(), peek(), is_empty(), len(stack)
    - pop() / peek() on an empty stack raise IndexError
    - repr(stack) -> "Stack([1, 2])"
    """

    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if not self._items:
            raise IndexError("peek at empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f"Stack({self._items})"


# ---------------------------------------------------------------------------
# Iterators & context managers  (__iter__/__next__, __enter__/__exit__)
# ---------------------------------------------------------------------------

class CountUp:
    """An ITERATOR class (no generators here!).
    - CountUp(start, stop) yields start, start+1, ..., stop (inclusive)
    - __iter__ returns self; __next__ raises StopIteration when done
    list(CountUp(1, 3)) -> [1, 2, 3]
    """

    def __init__(self, start, stop):
        self.current = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.stop:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


class Suppress:
    """A context manager that swallows the given exception types.
        with Suppress(ZeroDivisionError) as s:
            1 / 0
        s.caught -> the ZeroDivisionError instance   (None if nothing was raised)
    Other exception types must NOT be swallowed.
    Hint: __exit__ returns True to suppress an exception."""

    def __init__(self, *exception_types):
        self.exception_types = exception_types
        self.caught = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None and issubclass(exc_type, self.exception_types):
            self.caught = exc_value
            return True
        return False


# ---------------------------------------------------------------------------
# Dataclasses  (@dataclass, fields, defaults)
# ---------------------------------------------------------------------------

@dataclass
class InventoryItem:
    """Turn this into a @dataclass (from dataclasses import dataclass) and delete __init__.
    - fields: name: str, unit_price: float, quantity: int = 0
    - total_cost() -> unit_price * quantity
    The dataclass gives you __init__, __repr__ and __eq__ for free:
        repr(InventoryItem("pen", 1.5, 4)) -> "InventoryItem(name='pen', unit_price=1.5, quantity=4)"
    """

    name: str
    unit_price: float
    quantity: int = 0

    def total_cost(self):
        return self.unit_price * self.quantity


# ---------------------------------------------------------------------------
# Composition  (objects that contain other objects)
# ---------------------------------------------------------------------------

class Book:
    """
    - Book(title, author, isbn); .checked_out starts as False
    """

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = False


class Library:
    """Holds Book objects, keyed by isbn.
    - add_book(book): ValueError if a book with that isbn is already there
    - checkout(isbn): KeyError if unknown, ValueError if already checked out
    - return_book(isbn): KeyError if unknown, ValueError if it wasn't checked out
    - available_titles() -> sorted titles of books NOT checked out
    - books_by(author) -> titles by that author, in the order they were added
    - len(library) -> number of books
    """

    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if book.isbn in self.books:
            raise ValueError(f"a book with isbn {book.isbn} already exists")
        self.books[book.isbn] = book

    def checkout(self, isbn):
        book = self.books[isbn]
        if book.checked_out:
            raise ValueError(f"{book.title!r} is already checked out")
        book.checked_out = True

    def return_book(self, isbn):
        book = self.books[isbn]
        if not book.checked_out:
            raise ValueError(f"{book.title!r} was not checked out")
        book.checked_out = False

    def available_titles(self):
        return sorted(book.title for book in self.books.values() if not book.checked_out)

    def books_by(self, author):
        return [book.title for book in self.books.values() if book.author == author]

    def __len__(self):
        return len(self.books)


class ShoppingCart:
    """Holds Product objects (from above) with quantities.
    - add(product, quantity=1): adding the same product name again increases its quantity
    - remove(name): KeyError if it's not in the cart
    - .total property -> sum of price * quantity
    - len(cart) -> total number of items (sum of quantities)
    """

    def __init__(self):
        self.items = {}  # product name -> [product, quantity]

    def add(self, product, quantity=1):
        if product.name in self.items:
            self.items[product.name][1] += quantity
        else:
            self.items[product.name] = [product, quantity]

    def remove(self, name):
        del self.items[name]

    @property
    def total(self):
        return sum(product.price * quantity for product, quantity in self.items.values())

    def __len__(self):
        return sum(quantity for _, quantity in self.items.values())
