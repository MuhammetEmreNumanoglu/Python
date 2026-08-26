import unittest

def fizzbuzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    return str(n)

def calculate_tax(income, rate=0.2):
    if income < 0:
        raise ValueError("Income cannot be negative")
    return income * rate

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(9), "Fizz")

    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(10), "Buzz")

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(30), "FizzBuzz")

    def test_number(self):
        self.assertEqual(fizzbuzz(1), "1")
        self.assertEqual(fizzbuzz(7), "7")

class TestTax(unittest.TestCase):
    def test_basic(self):
        self.assertAlmostEqual(calculate_tax(1000), 200.0)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            calculate_tax(-100)

if __name__ == "__main__":
    unittest.main()
