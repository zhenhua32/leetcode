import unittest


class Queue:
    """在列表的最后位置移除元素, 在开头添加"""

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class TestQueue(unittest.TestCase):
    def test_queue(self):
        q = Queue()
        self.assertTrue(q.is_empty())
        q.enqueue(4)
        q.enqueue("dog")
        self.assertEqual(q.size(), 2)
        self.assertFalse(q.is_empty())
        q.enqueue(True)
        self.assertEqual(q.dequeue(), 4)
        self.assertEqual(q.dequeue(), "dog")
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.dequeue(), True)
        self.assertTrue(q.is_empty())
