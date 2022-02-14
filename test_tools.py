import unittest

from tools import Tools
from wordlist import wordlist_small


class TestToolsMethods(unittest.TestCase):
    def test_get_english_alphabet(self):
        tools = Tools()
        self.assertEqual(tools.get_english_alphabet(), {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'})

    def test_get_smaller_wordlist_zero(self):
        tools = Tools()
        self.assertEqual(tools.get_smaller_wordlist(wordlist_small, 0), [])
    
    def test_get_smaller_wordlist_one(self):
        tools = Tools()
        self.assertEqual(tools.get_smaller_wordlist(wordlist_small, 1), ['aback', 'bacon', 'cabal', 'daddy', 'eager', 'fable', 'gaffe', 'habit', 'icily', 'jaunt', 'kappa', 'label', 'macaw', 'nadir', 'oaken', 'paddy', 'quack', 'rabbi', 'sadly', 'tabby', 'udder', 'vague', 'wacky', 'yacht', 'zebra'])


if __name__ == '__main__':
    unittest.main()
