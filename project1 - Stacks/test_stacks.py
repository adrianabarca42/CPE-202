import unittest
from stacks import StackArray
from stacks import StackLinked
from Node import Node

class TestCase(unittest.TestCase):
    def test_stack_array(self):
        arr1 = StackArray()
        arr1.push(4)
        arr1.push(5)
        self.assertEqual(arr1.size(), 2)
        self.assertEqual(arr1.is_full(), True)
        arr1.enlarge()
        self.assertEqual(arr1.is_full(), False)
        arr1.push(6)
        arr1.push(7)
        self.assertEqual(arr1.is_full(), True)
        self.assertEqual(arr1.pop(), 7)
        arr1.pop()
        arr1.pop()
        arr1.pop()
        self.assertEqual(arr1.is_empty(), True)
        arr2 = StackArray()
        arr2.enlarge()
        arr2.enlarge()
        arr2.shrink()
        self.assertEqual(arr2.capacity, 4)
        arr2.enlarge()
        arr2.push(5)
        arr2.push(9)
        arr2.push(10)
        self.assertEqual(arr2.peek(), 10)
        arr3 = StackArray()
        self.assertEqual(arr3.peek(), None)
        print(arr2.arr)
        arr4 = StackArray()
        with self.assertRaises(IndexError):
            arr4.pop()

    def test_stack_linked(self):
        list = StackLinked()
        list.push(5)
        list.push(10)
        list.push(12)
        list.push(13)
        print(list)
        list.pop()
        self.assertEqual(list.pop(), 12)
        print(list)
        self.assertEqual(list.peek(), 10)
        list1 = StackLinked()
        self.assertEqual(list1.peek(), None)
        with self.assertRaises(IndexError):
            list1.pop()
        
def main():
    unittest.main()

if __name__ == '__main__':
    main()
