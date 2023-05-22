import math
import random
import unittest
from hw9_4 import my_factorial


class MyTest(unittest.TestCase):
    def test_factorial(self):
        number = random.randint(1, 20)
        self.assertEqual(my_factorial(number), math.factorial(number))

    def test_type(self):
        self.assertTrue(isinstance(my_factorial(5), int))


if __name__ == '__main__':
    unittest.main()
