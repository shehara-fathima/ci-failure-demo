import unittest
from src.main import add, divide

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_divide(self):
        # This test will fail when dividing by zero
        self.assertEqual(divide(10, 0), 0)

if __name__ == "__main__":
    unittest.main()
