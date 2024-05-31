import unittest
from ripasso import Calc

class TestCalculations(unittest.TestCase):

    def setUp(self):
        self.calculation = Calc(8,2)

    def test_sum(self):
        self.assertEqual(self.calculation.get_sum(), 10 ,'the sum is wrong')


if __name__ == '__main__':
    unittest.main()