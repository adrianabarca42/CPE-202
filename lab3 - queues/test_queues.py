import unittest
from queues import QueueArray
from queues import QueueLinked

class TestCase(unittest.TestCase):
    def test_queue_array(self):
        q1 = QueueArray(5)
        self.assertEqual(q1.is_empty(), True)
        q2 = QueueArray(1)
        q2.enqueue(4)
        print(q2)
        q3 = QueueArray(4)
        q3.enqueue(5)
        q3.enqueue(6)
        print(q3)
        self.assertEqual(q3.dequeue(), 5)
        q4 = QueueArray(3)
        q4.enqueue(1)
        q4.enqueue(2)
        q4.enqueue(3)
        print(q4)
        self.assertEqual(q4.is_full(), True)
        q4.dequeue()
        self.assertEqual(q4.size(), 2)
        q5 = QueueArray(2)
        q5.enqueue(0)
        q5.enqueue(1)
        q5.dequeue()
        q5.enqueue(2)
        print(q5)
        self.assertEqual(q5.is_full(), True)
        self.assertRaises(IndexError, q5.enqueue, 5)

    def test_queue_linked(self):
        q1 = QueueLinked(3)
        q1.enqueue(0)
        q1.enqueue(1)
        self.assertEqual(q1.size(), 2)
        q1.enqueue(2)
        self.assertEqual(q1.is_full(), True)
        
        
def main():
    unittest.main()

if __name__ == '__main__':
    main()
