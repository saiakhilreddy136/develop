import unittest
from main import to_upper

class MyTestCase(unittest.TestCase):
    def test_to_upper(self):
        self.assertEqual(to_upper("Vedasahithi"), "VEDASAHITHI")

if __name__ == '__main__':
    unittest.main()
