import unittest
from exercises import m04_oop as m


class TestOOP(unittest.TestCase):
    def test_bank_account_basic(self):
        acc = m.BankAccount("Asha", 100)
        acc.withdraw(40)
        self.assertEqual(acc.balance, 60)
        self.assertEqual(str(acc), "Asha: 60.00")
        self.assertEqual(acc.history, [("withdraw", 40)])

    def test_bank_account_errors(self):
        acc = m.BankAccount("Ravi")
        with self.assertRaises(ValueError):
            acc.deposit(0)
        with self.assertRaises(m.InsufficientFundsError):
            acc.withdraw(10)

    def test_savings_account(self):
        s = m.SavingsAccount("Meera", 1000, rate=0.1)
        self.assertIsInstance(s, m.BankAccount)
        s.add_interest()
        self.assertAlmostEqual(s.balance, 1100)
        self.assertEqual(s.history[-1][0], "deposit")

    def test_rectangle_properties(self):
        r = m.Rectangle(3, 4)
        self.assertEqual(r.area, 12)
        self.assertEqual(r.perimeter, 14)
        with self.assertRaises(ValueError):
            m.Rectangle(0, 5)

    def test_rectangle_eq_and_sort(self):
        self.assertEqual(m.Rectangle(2, 3), m.Rectangle(2, 3))
        rs = sorted([m.Rectangle(5, 5), m.Rectangle(1, 1), m.Rectangle(2, 3)])
        self.assertEqual([r.area for r in rs], [1, 6, 25])

    # --- Classes & instances ----------------------------------------------

    def test_person(self):
        p = m.Person("Asha", 17)
        self.assertEqual(p.greet(), "Hi, I'm Asha")
        self.assertFalse(p.is_adult())
        self.assertEqual(p.have_birthday(), 18)
        self.assertEqual(p.age, 18)
        self.assertTrue(p.is_adult())

    def test_click_counter(self):
        c = m.ClickCounter()
        self.assertEqual(c.increment().increment(5).value, 6)
        self.assertEqual(c.decrement(2).value, 4)
        self.assertEqual(c.decrement(10).value, 0)
        c2 = m.ClickCounter(10)
        c2.increment(3)
        c2.reset()
        self.assertEqual(c2.value, 10)

    # --- Properties & validation ------------------------------------------

    def test_temperature_properties(self):
        t = m.Temperature(100)
        self.assertAlmostEqual(t.fahrenheit, 212)
        t.fahrenheit = 32
        self.assertAlmostEqual(t.celsius, 0)
        t.celsius = 37
        self.assertAlmostEqual(t.fahrenheit, 98.6)
        with self.assertRaises(ValueError):
            t.celsius = -500
        with self.assertRaises(ValueError):
            m.Temperature(-300)

    def test_temperature_classmethod(self):
        t = m.Temperature.from_fahrenheit(212)
        self.assertIsInstance(t, m.Temperature)
        self.assertAlmostEqual(t.celsius, 100)

    def test_circle(self):
        c = m.Circle(2)
        self.assertAlmostEqual(c.area, 12.566370614359172)
        self.assertEqual(c.diameter, 4)
        c.diameter = 10
        self.assertEqual(c.radius, 5)
        with self.assertRaises(ValueError):
            c.radius = 0
        with self.assertRaises(ValueError):
            m.Circle(-1)
        with self.assertRaises(AttributeError):
            c.area = 3

    def test_user(self):
        u = m.User("asha", "supersecret")
        self.assertTrue(u.check_password("supersecret"))
        self.assertFalse(u.check_password("wrong"))
        self.assertEqual(str(u), "User(asha)")
        self.assertNotIn("supersecret", repr(u))
        with self.assertRaises(PermissionError):
            u.change_password("wrong", "newpassword")
        with self.assertRaises(ValueError):
            u.change_password("supersecret", "short")
        u.change_password("supersecret", "newpassword")
        self.assertTrue(u.check_password("newpassword"))
        with self.assertRaises(ValueError):
            m.User("bo", "1234")

    # --- Class attributes, classmethod, staticmethod ----------------------

    def test_employee_class_attributes(self):
        before = m.Employee.count
        a = m.Employee("Asha", 50000)
        b = m.Employee("Bo", 40000)
        self.assertEqual(m.Employee.count, before + 2)
        b.raise_amount = 1.10
        a.apply_raise()
        b.apply_raise()
        self.assertAlmostEqual(a.salary, 52500)
        self.assertAlmostEqual(b.salary, 44000)
        self.assertEqual(m.Employee.raise_amount, 1.05)

    def test_employee_class_and_static_methods(self):
        e = m.Employee.from_string("Asha-50000")
        self.assertIsInstance(e, m.Employee)
        self.assertEqual((e.name, e.salary), ("Asha", 50000))
        self.assertTrue(m.Employee.is_workday(0))
        self.assertTrue(m.Employee.is_workday(4))
        self.assertFalse(m.Employee.is_workday(6))

    # --- Inheritance & polymorphism ---------------------------------------

    def test_animals(self):
        rex, tom = m.Dog("Rex"), m.Cat("Tom")
        self.assertIsInstance(rex, m.Animal)
        self.assertEqual(rex.speak(), "Rex says Woof")
        self.assertEqual(rex.fetch(), "Rex fetches the ball")
        self.assertEqual(tom.speak(), "Tom says Meow (if it feels like it)")
        self.assertEqual(m.Animal("Moo", "Moo").speak(), "Moo says Moo")

    def test_shapes(self):
        shapes = [m.Square(2), m.Triangle(3, 4)]
        self.assertEqual(shapes[0].describe(), "Square with area 4.00")
        self.assertEqual(shapes[1].describe(), "Triangle with area 6.00")
        self.assertAlmostEqual(m.total_area(shapes), 10)
        self.assertEqual(m.total_area([]), 0)
        with self.assertRaises(NotImplementedError):
            m.Shape().area()

    # --- Abstract base classes & mixins -----------------------------------

    def test_payment_methods(self):
        self.assertEqual(m.CreditCard("1234567812345678").pay(50),
                         "Paid 50.00 with card ending 5678")
        self.assertEqual(m.PayPal("asha@example.com").pay(12.5),
                         "Paid 12.50 via PayPal (asha@example.com)")
        with self.assertRaises(TypeError):
            m.PaymentMethod()

        class Broken(m.PaymentMethod):
            pass
        with self.assertRaises(TypeError):
            Broken()

    def test_product_mixin(self):
        p = m.Product("pen", 1.5, 4)
        self.assertEqual(p.total_value, 6.0)
        self.assertEqual(p.to_dict(), {"name": "pen", "price": 1.5, "quantity": 4})
        self.assertEqual(p.to_json(), '{"name": "pen", "price": 1.5, "quantity": 4}')
        d = p.to_dict()
        d["price"] = 99
        self.assertEqual(p.price, 1.5, "to_dict() must return a copy")
        with self.assertRaises(ValueError):
            m.Product("bad", -1)

    # --- Dunder methods ---------------------------------------------------

    def test_vector_arithmetic(self):
        v1, v2 = m.Vector(1, 2), m.Vector(3, 4)
        self.assertEqual(v1 + v2, m.Vector(4, 6))
        self.assertEqual(v2 - v1, m.Vector(2, 2))
        self.assertEqual(v1 * 3, m.Vector(3, 6))
        self.assertEqual(3 * v1, m.Vector(3, 6))
        self.assertNotEqual(v1, v2)

    def test_vector_repr_abs_bool(self):
        self.assertEqual(repr(m.Vector(1, 2)), "Vector(1, 2)")
        self.assertEqual(abs(m.Vector(3, 4)), 5.0)
        self.assertFalse(m.Vector(0, 0))
        self.assertTrue(m.Vector(0, 1))

    def test_money(self):
        a, b = m.Money(10.5), m.Money(2.25)
        self.assertEqual(str(a), "10.50 USD")
        self.assertEqual(a + b, m.Money(12.75))
        self.assertTrue(b < a)
        self.assertTrue(a >= b)
        self.assertTrue(a <= m.Money(10.5))
        self.assertEqual(str(m.Money(3, "EUR")), "3.00 EUR")
        with self.assertRaises(ValueError):
            a + m.Money(1, "EUR")
        with self.assertRaises(ValueError):
            a < m.Money(1, "EUR")

    def test_fraction_basics(self):
        self.assertEqual(str(m.Fraction(2, 4)), "1/2")
        self.assertEqual(str(m.Fraction(1, -2)), "-1/2")
        self.assertEqual(str(m.Fraction(6, 2)), "3")
        self.assertEqual(m.Fraction(2, 4), m.Fraction(1, 2))
        self.assertEqual(float(m.Fraction(1, 4)), 0.25)
        with self.assertRaises(ZeroDivisionError):
            m.Fraction(1, 0)

    def test_fraction_arithmetic(self):
        self.assertEqual(m.Fraction(1, 2) + m.Fraction(1, 3), m.Fraction(5, 6))
        self.assertEqual(m.Fraction(2, 3) * m.Fraction(3, 4), m.Fraction(1, 2))
        self.assertEqual(str(m.Fraction(1, 2) + m.Fraction(1, 2)), "1")

    def test_playlist(self):
        p = m.Playlist("Road trip")
        for song in ["a", "b", "c", "d"]:
            p.add(song)
        self.assertEqual(len(p), 4)
        self.assertEqual(p[0], "a")
        self.assertEqual(p[-1], "d")
        self.assertEqual(list(p[1:3]), ["b", "c"])
        self.assertIn("c", p)
        self.assertNotIn("z", p)
        self.assertEqual([s for s in p], ["a", "b", "c", "d"])

    def test_stack(self):
        s = m.Stack()
        self.assertTrue(s.is_empty())
        s.push(1)
        s.push(2)
        self.assertEqual(repr(s), "Stack([1, 2])")
        self.assertEqual(len(s), 2)
        self.assertEqual(s.peek(), 2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)
        with self.assertRaises(IndexError):
            s.pop()
        with self.assertRaises(IndexError):
            s.peek()

    # --- Iterators & context managers -------------------------------------

    def test_count_up(self):
        self.assertEqual(list(m.CountUp(1, 3)), [1, 2, 3])
        it = m.CountUp(5, 5)
        self.assertIs(iter(it), it)
        self.assertEqual(next(it), 5)
        with self.assertRaises(StopIteration):
            next(it)
        self.assertEqual(list(m.CountUp(3, 1)), [])

    def test_suppress(self):
        with m.Suppress(ZeroDivisionError) as s:
            1 / 0
        self.assertIsInstance(s.caught, ZeroDivisionError)

        with m.Suppress(KeyError, IndexError) as s:
            [][0]
        self.assertIsInstance(s.caught, IndexError)

        with m.Suppress(ValueError) as s:
            pass
        self.assertIsNone(s.caught)

        with self.assertRaises(TypeError):
            with m.Suppress(ValueError):
                raise TypeError("not suppressed")

    # --- Dataclasses ------------------------------------------------------

    def test_inventory_item_dataclass(self):
        import dataclasses
        item = m.InventoryItem("pen", 1.5, 4)
        self.assertTrue(dataclasses.is_dataclass(m.InventoryItem), "use @dataclass")
        self.assertEqual(item.total_cost(), 6.0)
        self.assertEqual(repr(item), "InventoryItem(name='pen', unit_price=1.5, quantity=4)")
        self.assertEqual(item, m.InventoryItem("pen", 1.5, 4))
        self.assertEqual(m.InventoryItem("cup", 3.0).quantity, 0)

    # --- Composition ------------------------------------------------------

    def test_library_checkout(self):
        lib = m.Library()
        lib.add_book(m.Book("Dune", "Herbert", "111"))
        lib.add_book(m.Book("Emma", "Austen", "222"))
        self.assertEqual(len(lib), 2)
        with self.assertRaises(ValueError):
            lib.add_book(m.Book("Dune again", "Herbert", "111"))
        lib.checkout("111")
        self.assertEqual(lib.available_titles(), ["Emma"])
        with self.assertRaises(ValueError):
            lib.checkout("111")
        with self.assertRaises(KeyError):
            lib.checkout("999")
        lib.return_book("111")
        self.assertEqual(lib.available_titles(), ["Dune", "Emma"])
        with self.assertRaises(ValueError):
            lib.return_book("111")

    def test_library_books_by(self):
        lib = m.Library()
        lib.add_book(m.Book("Persuasion", "Austen", "1"))
        lib.add_book(m.Book("Dune", "Herbert", "2"))
        lib.add_book(m.Book("Emma", "Austen", "3"))
        self.assertEqual(lib.books_by("Austen"), ["Persuasion", "Emma"])
        self.assertEqual(lib.books_by("Nobody"), [])

    def test_shopping_cart(self):
        cart = m.ShoppingCart()
        cart.add(m.Product("pen", 1.5))
        cart.add(m.Product("book", 10), quantity=2)
        cart.add(m.Product("pen", 1.5), quantity=3)
        self.assertEqual(len(cart), 6)
        self.assertAlmostEqual(cart.total, 26.0)
        cart.remove("book")
        self.assertAlmostEqual(cart.total, 6.0)
        with self.assertRaises(KeyError):
            cart.remove("book")
