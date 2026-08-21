import unittest

class TestWithSetup(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3, 4, 5]
        self.config = {"limit": 10, "active": True}

    def tearDown(self):
        self.data = None

    def test_data_length(self):
        self.assertEqual(len(self.data), 5)

    def test_data_contains(self):
        self.assertIn(3, self.data)

    def test_config(self):
        self.assertTrue(self.config["active"])
        self.assertEqual(self.config["limit"], 10)

    def test_sum(self):
        self.assertEqual(sum(self.data), 15)

if __name__ == "__main__":
    unittest.main()
