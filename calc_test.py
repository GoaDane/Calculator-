from unittest import TestCase

class TestSum(TestCase):
    def test_sum(testcase):
        from calc import add


import unittest
from calc import calc

class CalculatorTest(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(4, self.calc.add(2,2))
        self.assertEqual(3.2, self.calc.add(1,2.2))

    def test_subtract(self):
        self.assertEqual(2, self.calc.subtract(3,1))
        self.assertEqual(-2, self.calc.subtract(1,3))

#    def test_multiple(self):
#        self.assertEqual(12, self.calc.multiple(3,4))
#        self.assertEqual(13.5, self.calc.multiple(3,4.5))

#    def test_devide(self):
#        self.assertEqual(3, self.calc.devide(9,3))

if __name__ == "main":
    unittest.main()
