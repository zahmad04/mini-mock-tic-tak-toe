import unittest
from subprocess import run

from main import *


class MyTest(unittest.TestCase):
    def test_output(self):
        result = run(["python", "main.py"], input=b"12\n", capture_output=True)
        self.assetEqual(result.stdout, b"Enter your age:You are 12 years old\n")
        
        
if __name__ == "__main__":
    unittest.main()