import unittest

class TestAssertions(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(1 + 1, 2)

    def test_not_equal(self):
        self.assertNotEqual(3, 4)

    def test_true(self):
        self.assertTrue(5 > 3)

    def test_false(self):
        self.assertFalse(3 > 5)

    def test_none(self):
        self.assertIsNone(None)

    def test_not_none(self):
        self.assertIsNotNone(42)

    def test_in(self):
        self.assertIn("hello", ["hello", "world"])

    def test_not_in(self):
        self.assertNotIn("foo", ["hello", "world"])

    def test_raises(self):
        with self.assertRaises(ZeroDivisionError):
            1 / 0

    def test_almost_equal(self):
        self.assertAlmostEqual(0.1 + 0.2, 0.3, places=5)

    def test_isinstance(self):
        self.assertIsInstance("hello", str)

if __name__ == "__main__":
    unittest.main()
