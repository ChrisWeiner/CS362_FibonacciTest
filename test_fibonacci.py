import unittest
import fibonacci as fib

class TestCaseFibonacci(unittest.TestCase):
    def test0(self):
        self.assertEqual(fib.fibonacci(0),0)
    def test1(self):
        self.assertEqual(fib.fibonacci(1),1)
    def test2(self):
        self.assertEqual(fib.fibonacci(2),1)
    def test3(self):
        self.assertEqual(fib.fibonacci(3),2)
    def test4(self):
        self.assertEqual(fib.fibonacci(4),3)
    def test5(self):
        self.assertEqual(fib.fibonacci(5),5)

class TestCaseFactorial(unittest.TestCase):
    def test1(self):
        self.assertEqual(fib.factorial(1),1)
    def test2(self):
        self.assertEqual(fib.factorial(2),2)
    def test3(self):
        self.assertEqual(fib.factorial(3),6)

#Purposeful failures using the unittest module, 
#class TestCaseExpectedFailure(unittest.TestCase):
#    @unittest.expectedFailure
#    def test0(self):
#        self.assertEqual(fib.fibonacci("failure"),1)
#    @unittest.expectedFailure
#    def test1(self):
#        self.assertEqual(fib.fibonacci(-1),1)

if __name__ == "__main__": #Using this line from the unittest lecture to display the number of failures in the test
    unittest.main(verbosity=2)