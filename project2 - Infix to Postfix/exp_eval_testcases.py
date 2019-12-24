import unittest
from exp_eval import infix_to_postfix, postfix_eval, postfix_valid
from stacks import StackLinked

class TestCase(unittest.TestCase):
    def test_infix_to_postfix(self):
        self.assertEqual(infix_to_postfix("( ~ 3 ) ^ 2"), "3 ~ 2 ^")
        self.assertEqual(infix_to_postfix("~ 3 ^ 2"), "3 2 ^ ~")
        self.assertEqual(infix_to_postfix("4 ^ ( ~ 1 ) * 4"), "4 1 ~ ^ 4 *")
        self.assertEqual(infix_to_postfix("~ 3 * 3 + 9"), "3 ~ 3 * 9 +")
        self.assertEqual(infix_to_postfix("( 3 * ( 4 + 6 / 3 ) )"), "3 4 6 3 / + *")
        self.assertEqual(infix_to_postfix("( ( 5 - 3 ) ^ 2 + ( 4 - 2 ) ^ 2 ) ^ ( 1 / 2 )"), "5 3 - 2 ^ 4 2 - 2 ^ + 1 2 / ^")
        self.assertEqual(infix_to_postfix("( ( 15 / ( 7 - ( 1 + 1 ) ) ) * 3 ) - ( 2 + ( 1 + 1 ) )"), "15 7 1 1 + - / 3 * 2 1 1 + + -")
        self.assertEqual(infix_to_postfix("10 + 3 * 5 / ( 16 - 4 )"), "10 3 5 * 16 4 - / +")
        self.assertEqual(infix_to_postfix("5 * 3 ^ ( 4 - 2 )"), "5 3 4 2 - ^ *")
        self.assertEqual(infix_to_postfix("( ( 1 * 2 ) + ( 3 / 4 ) )"), "1 2 * 3 4 / +")
        self.assertEqual(infix_to_postfix("( ( 2 * ( 3 + 4 ) ) / 5 )"), "2 3 4 + * 5 /")
        self.assertEqual(infix_to_postfix("~ 1"), "1 ~")
        self.assertEqual(infix_to_postfix("~ ~ 1"), "1 ~ ~")
        self.assertEqual(infix_to_postfix("1"), "1")

        
    def test_postfix_eval(self):
        self.assertEqual(postfix_eval("3 ~ 2 ^"), 9)
        self.assertEqual(postfix_eval("3 2 ^ ~ 9 +"), 0)
        self.assertEqual(postfix_eval("4 1 ~ ^ 4 *"), 1.0)
        self.assertRaises(ZeroDivisionError, postfix_eval, "5 0 /")
        self.assertEqual(postfix_eval("1 2 * 3 4 / +"), 2.75)
        self.assertEqual(postfix_eval("15 7 1 1 + - / 3 * 2 1 1 + + -"), 5)
        self.assertEqual(postfix_eval("5 3 - 2 ^ 4 2 - 2 ^ + 1 2 / ^"), 2.8284271247461903)
        self.assertEqual(postfix_eval("3 4 6 3 / + *"), 18)
        self.assertRaises(SyntaxError, postfix_eval, "5 + +")

    def test_postfix_valid(self):
        self.assertEqual(postfix_valid("4 1 ~ ^ 4 *"), True)
        self.assertEqual(postfix_valid("1 ~ ~"), True)
        self.assertEqual(postfix_valid("5 3 - 2 ^ 4 2 - 2 ^ + 1 2 / ^"), True)
        self.assertEqual(postfix_valid("~ 5 2 ^"), False)
        self.assertEqual(postfix_valid("15 7 1 1 + - / 3 * 2 1 1 + + -"), True)
        self.assertEqual(postfix_valid("( 3 * ( 4 + 6 / 3 ) )"), False)
        self.assertEqual(postfix_valid("3 ~ 3 * 9 +"), True)

def main():
    unittest.main()

if __name__ == '__main__':
    main()

    
