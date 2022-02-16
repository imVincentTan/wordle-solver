import unittest

from hint import Hint


class TestHintMethods(unittest.TestCase):
    def test_init(self):
        hint = Hint(5)
        self.assertEqual(hint.get_hints_key(), '-----')

    def test_set_green(self):
        hint = Hint(5)
        hint.set_green_hint(0)
        self.assertEqual(hint.get_hints_key(), 'g----')
    
    def test_set_yellow(self):
        hint = Hint(5)
        hint.set_yellow_hint(0)
        self.assertEqual(hint.get_hints_key(), 'y----')
    
    def test_set_grey(self):
        hint = Hint(5)
        hint.set_grey_hint(0)
        self.assertEqual(hint.get_hints_key(), 'x----')

    def test_combo(self):
        hint = Hint(5)
        hint.set_green_hint(1)
        hint.set_grey_hint(2)
        hint.set_yellow_hint(3)
        self.assertEqual(hint.get_hints_key(), '-gxy-')

    def test_is_unset_hint(self):
        hint = Hint(5)
        self.assertEqual(hint.is_unset_hint(0), True)

    def test_is_green_hint(self):
        hint = Hint(5)
        self.assertEqual(hint.is_green_hint(0), False)

    def test_is_yellow_hint(self):
        hint = Hint(5)
        self.assertEqual(hint.is_yellow_hint(0), False)

    def test_is_grey_hint(self):
        hint = Hint(5)
        self.assertEqual(hint.is_grey_hint(0), False)

    


if __name__ == '__main__':
    unittest.main()
