import unittest
from max_heap import insert, shift_up, shift_down, del_max, heapify, index_parent
from max_heap import index_left, index_right, index_maxchild
from heap_sort import sort

class TestCase(unittest.TestCase):
    def test_max_heap(self):
        arr = [None] * 5
        self.assertRaises(IndexError, insert, arr, 0, 6)
        insert(arr, 5, -1)
        insert(arr, 3, 0)
        insert(arr, 1, 1)
        insert(arr, 4, 2)
        insert(arr, 2, 3)
        print(arr)
        self.assertRaises(IndexError, insert, arr, 0, 4)
        end = len(arr) - 1
        arr, val, end = del_max(arr, end)
        self.assertEqual(val, 5)
        arr, val, end = del_max(arr, end)
        self.assertEqual(val, 4)
        arr, val, end = del_max(arr, end)
        self.assertEqual(val, 3)
        arr, val, end = del_max(arr, end)
        self.assertEqual(val, 2)
        arr = [1, 2, 3, 4, 5]
        print("arr = mh.heapify(", arr, ")")
        arr = heapify(arr)
        self.assertEqual(arr, [5, 4, 3, 1, 2])

    def test_heap_sort(self):
        arr = [1,3,2,5,4]
        self.assertEqual(sort(arr), [1,2,3,4,5])
        arr = [1,2,1,4,5]
        self.assertEqual(sort(arr), [1,1,2,4,5])
        arr = [1,2,3]
        self.assertEqual(sort(arr), [1,2,3])

def main():
    unittest.main()

if __name__ == '__main__':
    main()
