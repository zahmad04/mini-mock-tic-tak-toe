import unittest
from main import *


class MyTest(unittest.TestCase):
    def test(self):
        result = mySum(5, 4)
        self.assertEqual(result, 9, "Received {0} Expected {1}".format(result, 9))


if __name__ == "__main__":
    unittest.main()