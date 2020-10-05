from subprocess import run

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from main import *

class TestAssertionError(Exception):
    def __init__(self, expected, actual):
        self.expected = expected
        self.actual = actual

class TestResult:

    def __init__(self, name, status, expected, actual):
        self.name= name
        self.status = status
        self.expected = expected 
        self.actual = actual 


class TestEngine:
    
    def __init__(self):
        self.success = 0
        self.fails = 0
        self.results = []
    
    def setUp(self):
        print("\n\nRunning Tests.\n")

    def tearDown(self):
        print("Done.")

    def assertEqual(self, expected, actual, msg):
        if expected != actual:
            raise TestAssertionError(expected, actual)

    def runTest(self, fn):
        try:
            fn()
            self.results.append(TestResult( fn.__name__, "passed", None, None))

        except TestAssertionError as err:
            print(type(err), err)
            self.results.append(TestResult(
                fn.__name__, 
                "failed", 
                err.expected, 
                err.actual))
            

    def run(self):
        self.runTest(self.test_starter_1)
        self.runTest(self.test_starter_2)

        return self.results


    def test_starter_1(self):     
        result = run(["python", "./lesson-files/starter.py"], input=b"\n", capture_output=True)
        expected = b'20\n21\n22\n23\n24\n25\n26\n27\n28\n29\n'
        self.assertEqual(result.stdout, expected, "\nExpected:\n{0}\nReceived:\n{1}".format(expected, result.stdout))

    def test_starter_2(self):     
        result = run(["python", "./lesson-files/starter.py"], input=b"\n", capture_output=True)
        expected = b'20\n21\n22\n23\n24\n25\n26\n27\n28\n29\n30\n'
        self.assertEqual(result.stdout, expected, "\nExpected:\n{0}\nReceived:\n{1}".format(expected, result.stdout))



"""
    def test_variable_exists(self):
        self.assertNotEqual(pupil_age, None, "The variable pupil age has not been declared.")    
        
    def test_fn(self):
        self.assertEqual(mySum(5, 4), 9)
            
    def test_output(self):
        result = run(["python", "main.py"], input=b"12\n", capture_output=True)
        self.assertEqual(result.stdout, b"Enter your age:You are 12 years old\n", "Returned: {0}".format(result.stdout))        
"""

def textReset():
    print(u"\u001b[0m")

def textGreen():
    print(u"\u001b[32m")

def textRed():
    print(u"\u001b[31m")

def createTestSuite ():
    engine = TestEngine()

    results = engine.run()

    for result in results:
        
        if (result.status == "passed"):
            textGreen()
            print("{0}......Passed".format(result.name))
        else:
            textRed()
            print ("{0}.....Failed".format(result.name))
            print("Expected")
            print("========")
            print(result.expected)
        
            print("Actual")
            print("========")
            print(result.actual)
        
        textReset()
    

if __name__ == "__main__":
    createTestSuite()
