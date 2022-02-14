import unittest

from hints_calculator import HintsCalculator


class TestHintsCalculatorMethods(unittest.TestCase):
    def test_get_hints_0(self):
        hints_calculator = HintsCalculator('aback', 'bacon')
        self.assertEqual(hints_calculator.get_hints(), ['yellow','yellow','grey','yellow','grey'])

    def test_get_hints_1(self):
        hints_calculator = HintsCalculator('aabbc', 'edcba')
        self.assertEqual(hints_calculator.get_hints(), ['yellow','grey','grey','green','yellow'])


if __name__ == '__main__':
    unittest.main()
