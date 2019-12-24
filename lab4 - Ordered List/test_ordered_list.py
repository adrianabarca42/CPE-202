import unittest
from ordered_list import Node
from ordered_list import OrderedList

class TestCase(unittest.TestCase):
    def test_1(self):
        list1 = OrderedList()
        list1.add(1)
        list1.add(2)
        list1.add(3)
        print(list1)
        self.assertEqual(list1.search_forward(3), True)
        self.assertEqual(list1.search_backward(3), True)
        self.assertEqual(list1.search_forward(5), False)
        self.assertEqual(list1.search_backward(-1), False)
        self.assertEqual(list1.size(), 3)
        list2 = OrderedList()
        self.assertEqual(list2.is_empty(), True)
        self.assertEqual(list2.index(3), 2)
        list2.add(1)
        self.assertEqual(list2.pop(), 1)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
