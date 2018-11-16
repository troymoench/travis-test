import unittest


class TestString(unittest.TestCase):
    def test_string_lower(self):
        self.assertEqual("Hello".lower(), "hello")


if __name__ == "__main__":
    unittest.main()
