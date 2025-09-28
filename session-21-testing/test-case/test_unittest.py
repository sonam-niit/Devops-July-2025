import unittest
from calculator import add,sub

class CalculatorTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(-1,1),0)
        
        
## python -m unittest test_unittest.py