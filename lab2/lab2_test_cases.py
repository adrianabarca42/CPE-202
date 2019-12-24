import unittest
from lab2 import perm_lex

class TestCase(unittest.TestCase):
    def test_perm_lex(self):
        a_list = ["a"]
        self.assertEqual(perm_lex("a"), a_list)
        self.assertEqual(perm_lex(""), [])
        ab_list = ["ab", "ba"]
        self.assertEqual(perm_lex("ab"), ab_list)
        abc_list = ["abc", "acb", "bac", "bca", "cab", "cba"]
        self.assertEqual(perm_lex("abc"), abc_list)
        abcd_list = ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad',
'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca',
'dcab', 'dcba']
        self.assertEqual(perm_lex("abcd"), abcd_list)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
