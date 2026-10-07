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
